---
title: Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato
type: docs
weight: 20
url: /it/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/
---

## **Possibili Scenari di Utilizzo**

Puoi cambiare il **Numero di versione** del file Excel cliccando con il tasto destro sul file e selezionando Proprietà > Dettagli e poi modificando il campo **Numero di versione**. Usa la proprietà [**BuiltInDocumentPropertyCollection.document_version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/document_version) per cambiarlo programmaticamente utilizzando le API di Aspose.Cells for Python via .NET.

## **Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato**

Il codice di esempio seguente crea un workbook e modifica le proprietà del documento integrate che includono Titolo, Autori e numero di versione. Si prega di vedere il [file Excel di output](64716811.xlsx) generato dal codice e lo screenshot che mostra il Numero di versione modificato dalla proprietà [**BuiltInDocumentPropertyCollection.document_version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/document_version).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SpecifyDocumentVersionOfExcelFile.py" >}}

{{< app/cells/assistant language="python-net" >}}
