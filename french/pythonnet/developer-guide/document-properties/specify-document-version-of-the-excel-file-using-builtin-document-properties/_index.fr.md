---
title: Spécifier la version du document du fichier Excel en utilisant les propriétés de document intégrées
type: docs
weight: 20
url: /fr/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/
---

## **Scénarios d'utilisation possibles**

Vous pouvez changer le **numéro de version** du fichier Excel en cliquant avec le bouton droit sur le fichier puis en sélectionnant Propriétés > Détails et en modifiant le champ **Numéro de version**. Utilisez la propriété [**BuiltInDocumentPropertyCollection.document_version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/document_version) pour le modifier de manière programmatique avec les APIs de Aspose.Cells pour Python via .NET.

## **Spécifier la version du document du fichier Excel à l'aide des propriétés de document intégrées**

Le code d'exemple suivant crée un classeur et modifie ses propriétés de document intégrées qui incluent le titre, les auteurs et le numéro de version. Veuillez consulter le [fichier Excel de sortie](64716811.xlsx) généré par le code et la capture d'écran qui montre le numéro de version modifié par la propriété [**BuiltInDocumentPropertyCollection.document_version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/document_version).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SpecifyDocumentVersionOfExcelFile.py" >}}

{{< app/cells/assistant language="python-net" >}}
