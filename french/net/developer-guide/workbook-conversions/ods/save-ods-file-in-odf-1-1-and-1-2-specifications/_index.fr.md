---
title: Enregistrer un fichier ODS dans les spécifications ODF 1.1 et 1.2
linktitle: Enregistrer en tant que ODF 1.1 et 1.2 
description: Convertir Excel en spécifications ODF 1.1 et 1.2 avec Aspose.Cells.
type: docs
weight: 230
url: /fr/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge l'enregistrement d'un fichier ODS (OpenDocument Spreadsheet) selon les spécifications ODF (OpenDocument Format) 1.1 et 1.2. Aspose.Cells dispose de la propriété [**OdsSaveOptions.IsStrictSchema11**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/properties/isstrictschema11) qui spécifie l'utilisation de la spécification ODF 1.1 pour enregistrer les fichiers ODS. La valeur par défaut de cette propriété est **false**, donc le fichier ODS enregistré sans ce réglage utilise les spécifications 1.2.

{{% /alert %}}

Le code d'exemple ci-dessous crée un objet classeur, ajoute une valeur à la cellule A1 sur la première feuille de calcul, puis enregistre le fichier ODS selon les spécifications ODF 1.1 et 1.2. Par défaut, le fichier ODS est enregistré selon la spécification ODF 1.2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
