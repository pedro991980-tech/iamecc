const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Endpoint di test per verificare lo stato del server
app.get('/api/status', (req, res) => {
    res.json({
        status: 'online',
        project: 'IAmecc Backend',
        version: '1.0.0'
    });
});

// Endpoint base per il calcolo del preventivo anti-rincari
app.post('/api/quote/calculate', (req, res) => {
    const { partCost, laborHours, laborRate, inflationIndex } = req.body;
    
    // Algoritmo dinamico preventivo
    const adjustedPartCost = partCost * (1 + (inflationIndex || 0.05));
    const totalLabor = laborHours * laborRate;
    const finalTotal = adjustedPartCost + totalLabor;

    res.json({
        success: true,
        currency: 'EUR',
        breakdown: {
            basePartCost: partCost,
            adjustedPartCost: adjustedPartCost.toFixed(2),
            laborCost: totalLabor.toFixed(2),
            totalEstimate: finalTotal.toFixed(2)
        }
    });
});

app.listen(PORT, () => {
    console.log(`IAmecc Backend in ascolto sulla porta ${PORT}`);
});