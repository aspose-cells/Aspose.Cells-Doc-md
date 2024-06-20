---
title: Sottoreport
type: docs
weight: 20
url: /it/reportingservices/sub-reports/
---

{{% alert color="primary" %}} 

Abbiamo incluso il supporto per l'Incorporazione di un Sottoreport in una riga di gruppo della tabella. Il formato è:

&=subreport{ReportName=your report name; parameter1 name = parameter1 value; parameter2 name = parameter2 value;......} 

{{% /alert %}} 
### **Esempio**
**Un sottoreport in una tabella** 

![todo:image_alt_text](sub-reports_1.png)

Nell'esempio, il nome del sottoreport è “Dettaglio dell'ordine di vendita”. Ha un parametro, *NumeroOrdineDiVendita*. Il valore del parametro è *EmpSalesDetail.NumeroOrdineVendita.*
#### **Restrizioni sull'utilizzo dei Sottoreport**
- Il sottoreport deve essere progettato con lo strumento Aspose.Cells.Reporting Services Designer.
- Il Sottoreport può essere incorporato solo nella riga di gruppo della tabella e la riga del gruppo non può contenere altri elementi oltre al Sottoreport. Non è consentito incorporare un Sottoreport nelle righe di dettaglio o nel pie di pagina della tabella.
- Attualmente, non è supportata l'annidamento di più di un livello. Il Sottoreport non può contenere un report incorporato.
