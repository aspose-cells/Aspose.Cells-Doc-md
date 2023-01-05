---
title: Sotto-report
type: docs
weight: 20
url: /it/reportingservices/sub-reports/
---
{{% alert color="primary" %}} 

Abbiamo incorporato il supporto per l'incorporamento di un sottoreport in una riga del gruppo tabella. Il formato è:

&=subreport{ReportName=nome del tuo rapporto; parametro1 nome = parametro1 valore; nome parametro2 = valore parametro2;......} 

{{% /alert %}} 
### **Esempio**
**Un sottoreport in una tabella** 

![cose da fare:immagine_alt_testo](sub-reports_1.png)

 Nell'esempio, il nome del sottoreport è "Sales Order Detail". Ha un parametro,*Numero ordine vendite* . Il valore del parametro è*EmpSalesDetail.SalesOrderNumber.*
#### **Restrizioni sull'utilizzo dei sottoreport**
- Il sottoreport deve essere progettato con lo strumento Aspose.Cells.Reporting Services Designer.
- Il sottoreport può essere incorporato solo nella riga del gruppo di tabelle e la riga del gruppo non può contenere altri elementi tranne il sottoreport. Non è consentito incorporare un sottoreport nelle righe di dettaglio della tabella o nelle righe a piè di pagina.
- Attualmente, l'annidamento di più di un livello non è supportato. Il sottoreport non può contenere report incorporato.
