---
title: Converti Excel in ODS
type: docs
weight: 40
url: /it/python-java/convert-excel-to-ods/
---
## **Converti Excel in ODS**
I file ODS vengono creati dal programma Calc che fa parte di Apache OpenOffice Suite. I file ODS memorizzano i dati organizzati in righe e colonne e sono formattati utilizzando lo standard basato su XML OASIS OpenDocument.

Aspose.Cells for Python via Java supporta file ODS funzionanti. Gli esempi seguenti illustrano la conversione di Excel in un file ODS.
### **Conversione diretta**
Il modo più semplice per convertire un file Excel in ODS è caricare la cartella di lavoro e salvarla passando[SalvaFormato.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) come secondo parametro del[Cartella di lavoro.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) metodo.

Il frammento di codice seguente ha illustrato la conversione di Excel direttamente in ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Salvare il documento ODS nelle specifiche ODF 1.1 o 1.2**
Aspose.Cells for Python via Java supporta il salvataggio di file ODS nelle specifiche ODF 1.1 e ODF 1.2. Per questo, l'API fornisce[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) proprietà. Impostando questa proprietà su**VERO** salverà il file con la specifica ODF 1.1. Il valore predefinito di[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) è**falso**, quindi il file ODS salvato senza impostazioni speciali viene salvato con la specifica ODF 1.2.

Il seguente frammento di codice dimostra il salvataggio di file ODS con le specifiche ODF 1.1 e 1.2.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
