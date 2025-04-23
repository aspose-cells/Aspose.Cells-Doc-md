---
title: Enregistrer le fichier ODS selon les spécifications ODF 1.1, 1.2 et 1.3
type: docs
weight: 170
url: /fr/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells supporte la sauvegarde de fichiers ODS (Feuille de calcul OpenDocument) en format (**OpenDocument Format**) ODF 1.1, 1.2 et 1.3. Aspose.Cells a ajouté la propriété [**OdsSaveOptions.setOdfStrictVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions/#setOdfStrictVersion-int-) pour utiliser la version ODF lors de la sauvegarde des fichiers ODS. La valeur par défaut de cette propriété est [**OpenDocumentFormatVersionType.ODF_12**](https://reference.aspose.com/cells/java/com.aspose.cells/opendocumentformatversiontype/#ODF-12), donc un fichier ODS enregistré sans ces paramètres spéciaux utilisera la spécification 1.2.

{{% /alert %}}

Le code d'exemple ci-dessous crée un objet classeur, ajoute une valeur dans la cellule A1 de la première feuille de calcul, puis enregistre le fichier ODS dans les spécifications ODF 1.1 et 1.2. Par défaut, le fichier ODS est enregistré dans la spécification ODF 1.2.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
{{< app/cells/assistant language="java" >}}
