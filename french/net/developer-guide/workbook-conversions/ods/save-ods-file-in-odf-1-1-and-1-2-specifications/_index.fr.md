---
title: Enregistrer un fichier ODS conformément aux spécifications ODF 1.1, 1.2 et 1.3
linktitle: Enregistrer au format ODF 1.1, 1.2 et 1.3
description: Convertir Excel en spécifications ODF 1.1, 1.2 et 1.3 avec Aspose.Cells.
type: docs
weight: 230
url: /fr/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la sauvegarde d'un fichier ODS (**OpenDocument Spreadsheet**) dans les spécifications ODF (**OpenDocument Format**) 1.1, 1.2 et 1.3. Aspose.Cells dispose de la propriété [**OdsSaveOptions.OdfStrictVersion**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/odfstrictversion/) qui spécifie la version ODF pour la sauvegarde des fichiers ODS. La valeur par défaut de cette propriété est [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/net/aspose.cells.ods/opendocumentformatversiontype/), donc le fichier ODS enregistré sans cette configuration utilise la spécification 1.2.

{{% /alert %}}

Le code d'exemple ci-dessous crée un objet classeur, ajoute une valeur dans la cellule A1 de la première feuille de calcul, puis enregistre le fichier ODS selon les spécifications ODF 1.1, 1.2 et 1.3. Par défaut, le fichier ODS est enregistré selon la spécification ODF 1.2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
{{< app/cells/assistant language="csharp" >}}
