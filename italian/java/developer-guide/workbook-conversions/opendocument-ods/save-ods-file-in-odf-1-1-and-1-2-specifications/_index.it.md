---
title: Salva il file ODS in conformità alle Specifiche ODF 1.1, 1.2 e 1.3
type: docs
weight: 170
url: /it/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells supporta il salvataggio (file **OpenDocument Spreadsheet**) ODS in (**OpenDocument Format**) ODF 1.1, 1.2 e specifiche ODF 1.3. Aspose.Cells ha aggiunto la proprietà [**OdsSaveOptions.setOdfStrictVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions/#setOdfStrictVersion-int-) per usare la versione ODF per il salvataggio dei file ODS. Il valore predefinto di questa proprietà è [**OpenDocumentFormatVersionType.ODF_12**](https://reference.aspose.com/cells/java/com.aspose.cells/opendocumentformatversiontype/#ODF-12), quindi un file ODS salvato senza questa impostazione speciale utilizzerà la specifica 1.2.

{{% /alert %}}

Il codice di esempio di seguito crea l'oggetto del foglio di lavoro, aggiunge alcuni valori nella cella A1 del primo foglio di lavoro e quindi salva il file ODS nelle specifiche ODF 1.1 e 1.2. Per impostazione predefinita, il file ODS viene salvato nelle specifiche ODF 1.2.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
{{< app/cells/assistant language="java" >}}
