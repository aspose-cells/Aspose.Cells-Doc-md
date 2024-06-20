---
title: Enregistrer un fichier ODS dans les spécifications ODF 1.1 et 1.2
linktitle: Enregistrer en tant que ODF 1.1 et 1.2 
description: Convertir Excel en spécifications ODF 1.1 et 1.2 avec Aspose.Cells.
type: docs
weight: 230
url: /fr/python-net/save-ods-file-in-odf-1-1-and-1-2-specifications/
description: Comment enregistrer un fichier ODS dans les spécifications ODF 1.1 et 1.2 avec l API Aspose.Cells pour Python via .NET.
keywords: Enregistrer un fichier ODS dans les spécifications ODF 1.1 et 1.2 avec Python, Enregistrer un fichier ODS dans les spécifications ODF 1.1 et 1.2 Pyton via NET.
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET prend en charge l'enregistrement d'un fichier ODS (**OpenDocument Spreadsheet**) dans les spécifications ODF (**OpenDocument Format**) 1.1 et 1.2. Aspose.Cells pour Python via .NET dispose d'une propriété [**OdsSaveOptions.is_strict_schema11**](https://reference.aspose.com/cells/python-net/aspose.cells/odssaveoptions/is_strict_schema11/) qui spécifie l'utilisation de la spécification ODF 1.1 pour l'enregistrement des fichiers ODS. La valeur par défaut de cette propriété est **false**, donc le fichier ODS enregistré sans ce paramètre utilise les spécifications 1.2.

{{% /alert %}}

Le code d'exemple ci-dessous crée un objet classeur, ajoute une valeur à la cellule A1 sur la première feuille de calcul, puis enregistre le fichier ODS selon les spécifications ODF 1.1 et 1.2. Par défaut, le fichier ODS est enregistré selon la spécification ODF 1.2.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.py" >}}
