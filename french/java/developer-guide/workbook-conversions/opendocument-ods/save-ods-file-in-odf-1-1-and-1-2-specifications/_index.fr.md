---
title: Enregistrer un fichier ODS dans les spécifications ODF 1.1 et 1.2
type: docs
weight: 170
url: /fr/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge l'enregistrement du fichier ODS (**OpenDocument Spreadsheet**) dans les spécifications ODF 1.1 et ODF 1.2. Aspose.Cells a ajouté la propriété [**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11) pour utiliser la spécification ODF 1.1 pour l'enregistrement des fichiers ODS. La valeur par défaut de cette propriété est **false**, donc le fichier ODS enregistré sans ce réglage spécial utilisera la spécification 1.2.

{{% /alert %}}

Le code d'exemple ci-dessous crée un objet classeur, ajoute une valeur dans la cellule A1 de la première feuille de calcul, puis enregistre le fichier ODS dans les spécifications ODF 1.1 et 1.2. Par défaut, le fichier ODS est enregistré dans la spécification ODF 1.2.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
