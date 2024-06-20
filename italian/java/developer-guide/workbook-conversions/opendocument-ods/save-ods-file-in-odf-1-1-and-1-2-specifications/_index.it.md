---
title: Salva il file ODS nelle specifiche ODF 1.1 e 1.2
type: docs
weight: 170
url: /it/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells supporta il salvataggio (**OpenDocument Spreadsheet**) del file ODS nelle specifiche (**OpenDocument Format**) ODF 1.1 e ODF 1.2. Aspose.Cells ha aggiunto la proprietà [**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11) per utilizzare la specifica ODF 1.1 per il salvataggio dei file ODS. Il valore predefinito di questa proprietà è **false**, quindi il file ODS salvato senza queste impostazioni speciali utilizzerà la specifica 1.2.

{{% /alert %}}

Il codice di esempio di seguito crea l'oggetto del foglio di lavoro, aggiunge alcuni valori nella cella A1 del primo foglio di lavoro e quindi salva il file ODS nelle specifiche ODF 1.1 e 1.2. Per impostazione predefinita, il file ODS viene salvato nelle specifiche ODF 1.2.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
