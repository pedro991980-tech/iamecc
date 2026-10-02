const PDFDocument = require('pdfkit');
const fs = require('fs');

function generateProfessionalQuote(quoteData, outputPath) {
    return new Promise((resolve, reject) => {
        const doc = new PDFDocument({ margin: 50 });
        const stream = fs.createWriteStream(outputPath);
        doc.pipe(stream);

        // Intestazione Preventivo / Brand Officina
        doc.fillColor('#161B22').fontSize(20).text('IAmecc - Preventivo di Riparazione', { align: 'left' });
        doc.fontSize(10).text(`Data: ${new Date().toLocaleDateString()}`, { align: 'left' });
        doc.moveDown();

        // Dettagli Veicolo e Diagnosi AI
        doc.fontSize(14).text('1. Diagnosi e Dettagli Veicolo', { underline: true });
        doc.fontSize(10).text(`Veicolo: ${quoteData.vehicleModel} (Targa/VIN: ${quoteData.vin})`);
        doc.text(`Anomalia Rilevata dall'IA: ${quoteData.aiDiagnosis}`);
        doc.moveDown();

        // Tabella Costi (Ricambi e Manodopera)
        doc.fontSize(14).text('2. Scomposizione Costi e Ricambi', { underline: true });
        doc.fontSize(10).text(`Ricambio: ${quoteData.partName} (Codice OE: ${quoteData.partCode})`);
        doc.text(`Costo Ricambio (Aggiornato listino): € ${quoteData.adjustedPartCost}`);
        doc.text(`Manodopera (${quoteData.laborHours} ore): € ${quoteData.laborCost}`);
        doc.moveDown();

        // Totale Finale Anti-Rincari
        doc.fontSize(14).fillColor('#004225').text(`Totale Preventivo: € ${quoteData.finalTotal}`, { align: 'right' });
        
        // Chiusura documento
        doc.end();
        
        stream.on('finish', () => resolve(outputPath));
        stream.on('error', (err) => reject(err));
    });
}

module.exports = { generateProfessionalQuote };