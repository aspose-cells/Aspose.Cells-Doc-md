---
title: Spécifier la version du document Excel en utilisant les propriétés intégrées du document avec Golang via C++
linktitle: Spécifier la version du document
type: docs
weight: 20
url: /fr/go-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Apprenez comment spécifier la version d un fichier Excel en utilisant les propriétés de document intégrées avec Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez modifier le **Numéro de version** d'un fichier Excel en cliquant avec le bouton droit sur le fichier, en sélectionnant Propriétés > Détails, puis en modifiant le champ **Numéro de version**. Utilisez la propriété [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getdocumentversion/) pour le changer de manière programmatique avec les API Aspose.Cells.

## **Spécifier la version du document du fichier Excel à l'aide des propriétés de document intégrées**

Le code d'exemple suivant crée un classeur et modifie ses propriétés de document intégrées, notamment Titre, Auteurs et Numéro de version. Veuillez consulter le [fichier Excel de sortie](64716811.xlsx) généré par le code et la capture d'écran qui montre la modification du numéro de version avec la propriété [**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getdocumentversion/).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyDocumentVersionOfTheExcelFileUsingBuiltinDocumentProperties.go" >}}
