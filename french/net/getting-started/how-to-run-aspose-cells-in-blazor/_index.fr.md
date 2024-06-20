---
title: Comment exécuter Aspose.Cells dans Blazor
type: docs
weight: 138
url: /fr/net/how-to-run-aspose-cells-in-blazor/
description: Apprenez à exécuter Aspose.Cells dans Blazor.
keywords: Exécuter Aspose.Cells en C# dans Blazor, Utiliser Aspose.Cells dans Blazor, Application de serveur Blazor avec Aspose.Cells
---

## Aperçu

Pour exécuter Aspose.Cells dans Blazor, vous avez besoin de plateformes .NET6 (ou ultérieures), comparez aux plateformes précédentes (.netcore31 ou antérieures), une différence importante concerne la bibliothèque graphique. Dans ce document officiel de [Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), il explique que pour les versions .NET6 ou ultérieures, la bibliothèque graphique "System.Drawing.Common" ne sera supportée que sur Windows, et donne des recommandations pour remplacer la bibliothèque graphique.

Pour le produit Aspose.Cells, nous avons effectué l'évaluation et avons terminé la migration de la bibliothèque graphique. Nous utilisons SkiaSharp au lieu de System.Drawing.Common dans les systèmes non-Windows, comme suggéré dans la documentation officielle de Microsoft. Veuillez noter que ce changement critique prendra effet dans Aspose.Cells 22.10.1 ou ultérieur pour .Net6.

## Application de serveur Blazor avec Aspose.Cells

Dans cet exemple, vous créez une application serveur Blazor simple qui ajoute des données et des graphiques, et les rend sous forme d'images pour les afficher sur la page web. Pendant le processus de création du projet, vous pouvez configurer les options selon vos besoins. Par exemple, lorsque vous cochez l'option "Activer Docker", l'application Blazor peut ensuite être construite et exécutée dans Docker..

### Créer une application de serveur Blazor

Utilisons l'outil VS2022 comme exemple pour créer la première application blazor avec Aspose.Cells, suivez les étapes ci-dessous:
1. Sélectionnez Fichier -> Nouveau -> Projet et filtrez en utilisant le mot-clé blazer pour sélectionner le modèle de projet correspondant.
<br>
<img src="1.png" width=70% />
1. Définissez le nom du projet sur "BlazorTest" et sélectionnez le chemin.
<br>
<img src="2.png" width=70% />
1. Configurez les bibliothèques et autres options utilisées dans le projet. Enfin, cliquez sur le bouton "Créer" pour générer votre premier projet blazer.
<br>
<img src="3.png" width=70% />
1. Après avoir entré dans le projet, cliquez sur "Dépendances" sous le projet et sélectionnez "Gérer les packages NuGet..." pour ajouter la bibliothèque Aspose.Cells.
<br>
<img src="4.png" width=70% />
1. Entrez des mots-clés pour filtrer et installez la dernière bibliothèque Aspose.Cells. Des bibliothèques dépendantes telles que SkiaSharp seront également installées ensemble.
<br>
<img src="5.png" width=70% />
1. Double-cliquez sur le fichier "Index.razor" pour éditer et importer la bibliothèque requise. Ajoutez des données et des graphiques, et affichez-les sous forme de graphiques.
<br>
<img src="5.png" width=70% />
1. Compilez et exécutez le projet, et vous obtiendrez les résultats suivants.
<br>
<img src="7.png" width=70% />

### Exemple de code dans l'application Blazor Server

Le code d'exemple suivant est inclus dans le fichier Index.razor:
```
@page "/"
@using SkiaSharp;
@using Aspose.Cells;
@using Aspose.Cells.Drawing;
@using Aspose.Cells.Rendering;


<PageTitle>Index</PageTitle>

<h1>Hello, world!</h1>

Welcome to your new app.

<SurveyPrompt Title="How is Blazor working for you?" />

<img src="@imageSrc" />

@code
{
    private string imageSrc;

    public Index()
    {
        imageSrc = "data:image/png;base64, " + Convert.ToBase64String(CreateFile());
    }

    private byte[] CreateFile()
    {
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        sheet.Cells["A1"].Value = "test data for blazor";

        sheet.PageSetup.PrintGridlines = true;
        sheet.PageSetup.PrintArea = "A1:F20";

        ShapeCollection shapes = sheet.Shapes;

        //Add rectangle shape
        shapes.AddRectangle(1, 0, 1, 0, 100, 150);

        //Add line shape
        shapes.AddLine(8, 0, 1, 0, 100, 150);

        //Add oval shape
        shapes.AddOval(13, 0, 1, 0, 100, 150);

        using MemoryStream ms = new();

        SheetRender render = new SheetRender(sheet, new ImageOrPrintOptions());
        render.ToImage(0, ms);

        return ms.ToArray();
    }
}

```
