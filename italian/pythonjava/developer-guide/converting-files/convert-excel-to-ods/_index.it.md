---
title: Converti Excel in ODS
type: docs
weight: 40
url: /it/python-java/convert-excel-to-ods/
---

## **Converti Excel in ODS**
I file ODS sono creati dal programma Calc, che fa parte del pacchetto Apache OpenOffice. I file ODS memorizzano dati organizzati in righe e colonne e sono formattati utilizzando lo standard XML OpenDocument OASIS.

Aspose.Cells per Python via Java supporta il lavoro con file ODS. Gli esempi seguenti mostrano come convertire Excel in un file ODS.
### **Conversione Diretta**
Il modo più semplice per convertire un file di Excel in ODS è caricare il foglio di lavoro e salvarlo passando [SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) come secondo parametro del metodo [Workbook.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)).

Il seguente frammento di codice mostra come convertire Excel direttamente in ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Salva il documento ODS nelle specifiche ODF 1.1 o 1.2.**
Aspose.Cells per Python via Java supporta il salvataggio dei file ODS nelle specifiche ODF 1.1 e ODF 1.2. A tal scopo, l'API fornisce la proprietà [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11). Impostando questa proprietà su **true** si salverà il file con le specifiche ODF 1.1. Il valore predefinito di [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) è **false**, quindi il file ODS salvato senza impostazioni speciali è salvato con le specifiche ODF 1.2.

Il seguente frammento di codice mostra il salvataggio dei file ODS con le specifiche ODF 1.1 e 1.2.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
