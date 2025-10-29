---
title: Enregistrer un fichier ODS dans les spécifications ODF 1.1, 1.2 et 1.3 avec Golang via C++
linktitle: Enregistrer en tant que ODF 1.1, 1.2 et 1.3
description: Convertir Excel en spécifications ODF 1.1, 1.2 et 1.3 avec Aspose.Cells en C++.
type: docs
weight: 230
url: /fr/go-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la sauvegarde d'un fichier ODS (**OpenDocument Spreadsheet**) dans les spécifications ODF (**OpenDocument Format**) 1.1, 1.2 et 1.3. Aspose.Cells dispose de la propriété [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/go-cpp/odssaveoptions/getodfstrictversion/) qui spécifie la version ODF pour la sauvegarde des fichiers ODS. La valeur par défaut de cette propriété est [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/), donc le fichier ODS enregistré sans cette configuration utilise la spécification 1.2.

{{% /alert %}}

Le code d'exemple ci-dessous crée un objet classeur, ajoute une valeur dans la cellule A1 de la première feuille de calcul, puis enregistre le fichier ODS selon les spécifications ODF 1.1, 1.2 et 1.3. Par défaut, le fichier ODS est enregistré selon la spécification ODF 1.2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveOdsFileInOdf11And12Specifications.go" >}}
