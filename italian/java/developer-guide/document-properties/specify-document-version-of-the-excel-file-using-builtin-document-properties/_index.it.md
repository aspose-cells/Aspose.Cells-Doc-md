---
title: Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato
type: docs
weight: 20
url: /it/java/specify-document-version-of-the-excel-file-using-builtin-document-properties/
---

## **Possibili Scenari di Utilizzo**

È possibile modificare il *numero di versione* del file Excel facendo clic destro sul file e quindi selezionando *Proprietà > Dettagli* e quindi modificando il campo *Numero di versione*. Si prega di utilizzare la proprietà [**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#DocumentVersion) per modificarlo in modo programmato utilizzando le API Aspose.Cells.

## **Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato**

Il seguente codice di esempio crea un workbook e modifica le sue proprietà di documento incorporate che includono *Titolo*, *Autori* e *Numero di versione*. Si prega di vedere il [file Excel di output](64716836.xlsx) generato dal codice e lo screenshot che mostra il *Numero di versione* modificato dalla proprietà [**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#DocumentVersion).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SpecifyDocumentVersionOfExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
