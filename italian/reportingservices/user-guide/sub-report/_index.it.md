---
title: Sottoreport
type: docs
weight: 90
url: /it/reportingservices/sub-report/
---

{{% alert color="primary" %}} 

Un sottoreport può essere incorporato in un elemento tabella. Il formato è: &=subreport{ReportName=nome del tuo report; parametro1 nome = valore del parametro1; parametro2 nome = valore del parametro2; ...}

**Un sottoreport in una definizione di report** 

![todo:image_alt_text](sub-report_1.png)

Nell'esempio, il nome del sottoreport è 'Dettaglio dell'ordine di vendita'. Ha un parametro, NumeroOrdineVendita. Il valore del parametro è EmpSalesDetail.SalesOrderNumber.
### **Limitazioni sui Sottoreport**
1. Il sottoreport deve essere progettato con Aspose.Cells.ReportingServices Designer.
1. Il sottoreport può essere inserito solo nella riga di gruppo della tabella e la riga di gruppo non può contenere nessun elemento tranne il sottoreport. L'incorporazione di un sottoreport nelle righe di dettaglio o nelle righe di piè di pagina della tabella non è consentita.
1. Attualmente, l'annidamento di più livelli non è supportato. Il sottoreport non può contenere un report incorporato.

{{% /alert %}} 
###### **Questa sezione include i seguenti argomenti:** 
- [Creazione di Elemento Tabella](/cells/it/reportingservices/creating-table-item/)
- [Aggiungi Elemento Sottoreport](/cells/it/reportingservices/add-sub-report-item/)
