---  
title: Applicare Filtro Avanzato di Microsoft Excel per Visualizzare Record che Soddisfano Criteri Complessi
type: docs  
weight: 280  
url: /it/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/  
description: Scopri come applicare il filtro avanzato di Microsoft Excel per visualizzare record che soddisfano criteri complessi utilizzando l API Aspose.Cells for Node.js via C++.  
keywords: Applica il Filtro Avanzato Node.js tramite C++, Imposta il Filtro Avanzato Node.js tramite C++, Aggiungi il Filtro Avanzato Node.js tramite C++, Crea il Filtro Avanzato Node.js tramite C++, Come aggiungere il Filtro Avanzato a un intervallo Node.js tramite C++  
---  

## **Possibili Scenari di Utilizzo**  

Microsoft Excel ti permette di applicare *Filtro Avanzato* sui dati del foglio di lavoro per visualizzare record che soddisfano criteri complessi. Puoi applicare il filtro avanzato con Microsoft Excel tramite il comando *Dati > Avanzate* come mostrato in questo screenshot.  

![todo:image_alt_text](1.png)  

Aspose.Cells for Node.js via C++ permette anche di applicare il Filtro Avanzato usando il metodo [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-). Come Microsoft Excel, accetta i seguenti parametri.  

**isFilter**  

Indica se filtrare l'elenco sul posto.  

**listRange**  

L'intervallo dell'elenco.  

**criteriaRange**  

L'intervallo dei criteri.  

**copyTo**  

L'intervallo in cui copiare i dati.  

**uniqueRecordOnly**  

Mostra o copia solo le righe uniche.  

## **Applicare il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi**  

Il seguente esempio di codice applica il filtro avanzato sul [File Excel di esempio](48496692.xlsx) e genera il [File Excel di output](48496691.xlsx). Lo screenshot mostra entrambi i file per confronto. Come si può vedere nello screenshot, i dati sono stati filtrati all'interno del file Excel di output secondo criteri complessi.  

![todo:image_alt_text](2.png)  

## **Codice di Esempio**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-AdvancedFilter.js" >}}


