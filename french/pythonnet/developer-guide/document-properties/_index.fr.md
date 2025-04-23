---
title: Gérer les propriétés de document
linktitle: Propriétés de document
type: docs
weight: 80
url: /fr/python-net/managing-document-properties/
description: Apprenez comment gérer les propriétés du document via l API Aspose.Cells pour Python via .NET.
keywords: Comment gérer les propriétés du document en C#, obtenir ou définir des propriétés de document en C#, ajouter ou supprimer des propriétés de document via C#, insérer ou supprimer des propriétés de document avec C#, comment accéder aux propriétés du document via Aspose.Cells pour Python via .NET API.
---


## **Introduction**

Microsoft Excel permet d'ajouter des propriétés aux fichiers de feuille de calcul. Ces propriétés de document fournissent des informations utiles et sont divisées en 2 catégories comme détaillé ci-dessous.

- Propriétés système définies (intégrées) : Les propriétés intégrées contiennent des informations générales sur le document telles que le titre du document, le nom de l'auteur, les statistiques du document, etc.
- Propriétés utilisateur définies (personnalisées) : Propriétés personnalisées définies par l'utilisateur final sous forme de paire nom-valeur.

{{% alert color="primary" %}}

Le point le plus important à savoir sur les propriétés intégrées et personnalisées est que les propriétés intégrées peuvent être consultées et modifiées, mais pas créées ou supprimées. Cependant, les propriétés personnalisées peuvent être créées et gérées.

{{% /alert %}}

## **Comment gérer les propriétés de document à l'aide de Microsoft Excel**

Microsoft Excel vous permet de gérer les propriétés de document des fichiers Excel de manière WYSIWYG. Veuillez suivre les étapes ci-dessous pour ouvrir la boîte de dialogue **Propriétés** dans Excel 2016.

1. Dans le menu **Fichier**, sélectionnez **Infos**.

|**Sélection du menu Infos**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Cliquez sur le titre **Propriétés** et sélectionnez "Propriétés avancées".

|**Cliquez pour sélectionner les propriétés avancées**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Gérez les propriétés de document du fichier.

|**Boîte de dialogue des propriétés**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
Dans la boîte de dialogue des propriétés, il y a différents onglets, comme Général, Résumé, Statistiques, Contenu et Personnalisés. Chaque onglet aide à configurer différents types d'informations liées au fichier. L'onglet Personnalisé est utilisé pour gérer les propriétés personnalisées.

## **Comment travailler avec les propriétés de document à l'aide d'Aspose.Cells**

Les développeurs peuvent gérer dynamiquement les propriétés du document à l'aide de l'API Aspose.Cells pour Python via .NET. Cette fonctionnalité aide les développeurs à stocker des informations utiles avec le fichier, comme la date de réception, de traitement, l'horodatage, etc.

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET écrit directement les informations sur l'API et le Numéro de Version dans les documents de sortie. Par exemple, lors de la conversion d’un document en PDF, Aspose.Cells pour Python via .NET remplit le champ **Application** avec la valeur 'Aspose.Cells' et le champ **PDF Producer** avec, par exemple, 'Aspose.Cells pour Python via .NET v17.9'.

Veuillez noter que vous ne pouvez pas demander à Aspose.Cells pour Python via .NET de modifier ou supprimer ces informations dans les documents de sortie.

{{% /alert %}}


### **Comment ajouter ou supprimer des propriétés de document personnalisées**

Comme nous l'avons décrit précédemment au début de ce sujet, les développeurs ne peuvent pas ajouter ou supprimer des propriétés intégrées car ces propriétés sont système-définies, mais il est possible d'ajouter ou de supprimer des propriétés personnalisées car celles-ci sont définies par l'utilisateur.

### **Comment ajouter des propriétés personnalisées**

Les API Aspose.Cells pour Python via .NET ont exposé la méthode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) pour la classe [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection) afin d'ajouter des propriétés personnalisées à la collection. La méthode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) ajoute la propriété au fichier Excel et retourne une référence pour la nouvelle propriété de document en tant qu'objet [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/documentproperty).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingDocumentProperties.py" >}}


## **Sujets avancés**
- [Ajout de propriétés personnalisées visibles dans le volet Informations sur le document](/cells/fr/python-net/adding-custom-properties-visible-inside-document-information-panel/)
- [Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.](/cells/fr/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Spécifier la version du document du fichier Excel à l'aide des propriétés de document intégrées](/cells/fr/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Spécifier la langue du fichier Excel en utilisant les propriétés de document intégrées](/cells/fr/python-net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

