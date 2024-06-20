---
title: Spécifier la version du document du fichier Excel en utilisant les propriétés de document intégrées
type: docs
weight: 20
url: /fr/java/specify-document-version-of-the-excel-file-using-builtin-document-properties/
---

## **Scénarios d'utilisation possibles**

Vous pouvez changer le * numéro de version * du fichier Excel en cliquant avec le bouton droit sur le fichier, puis en sélectionnant * Propriétés > Détails * et en modifiant le champ * Numéro de version *. Veuillez utiliser la propriété [**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#DocumentVersion) pour le modifier de manière programmatique à l'aide des API Aspose.Cells.

## **Spécifier la version du document du fichier Excel à l'aide des propriétés de document intégrées**

Le code d'exemple suivant crée un classeur et modifie ses propriétés de document incorporées qui comprennent *Titre*, *Auteurs* et *Numéro de version*. Veuillez consulter le [fichier Excel de sortie](64716836.xlsx) généré par le code et la capture d'écran qui montre le champ *Numéro de version* modifié par la propriété [**BuiltInDocumentPropertyCollection.DocumentVersion**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#DocumentVersion).

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SpecifyDocumentVersionOfExcelFile.java" >}}
