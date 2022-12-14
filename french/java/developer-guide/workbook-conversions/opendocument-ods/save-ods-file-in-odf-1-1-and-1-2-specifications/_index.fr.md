---
title: Enregistrer le fichier ODS dans les spécifications ODF 1.1 et 1.2
type: docs
weight: 170
url: /fr/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---
{{% alert color="primary" %}}

Aspose.Cells prend en charge l'enregistrement (**Feuille de calcul OpenDocument**) Fichier ODS dans (**Format OpenDocument** ) Spécifications ODF 1.1 et ODF 1.2. Aspose.Cells a ajouté[**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11) propriété pour utiliser la spécification ODF 1.1 pour enregistrer les fichiers ODS. La valeur par défaut de cette propriété est**faux**, donc le fichier ODS enregistré sans ces paramètres spéciaux utilisera la spécification 1.2.

{{% /alert %}}

L'exemple de code ci-dessous crée l'objet classeur, ajoute une valeur dans la cellule A1 de la première feuille de calcul, puis enregistre le fichier ODS dans les spécifications ODF 1.1 et 1.2. Par défaut, le fichier ODS est enregistré dans la spécification ODF 1.2.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
