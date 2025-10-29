---
title: HTML avec C++
linktitle: HTML
type: docs
weight: 230
url: /fr/cpp/convert-excel-to-html/
description: Convertir Excel en format HTML et MHTML en utilisant Aspose.Cells avec C++.
---

## **Conversion de Classeur Excel en HTML**
L’API Aspose.Cells offre un support pour l’exportation de feuilles de calcul au format HTML. À cette fin, Aspose.Cells utilise la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions) pour offrir la flexibilité de contrôler plusieurs aspects du HTML de sortie.

L'exemple de code ci-dessous montre comment enregistrer un classeur au format HTML en utilisant C++ :

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"Book1.xlsx");

    // Save file to HTML format
    workbook.Save(u"out.html");

    std::cout << "Workbook saved to HTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Conversion de Classeur Excel en Fichiers MHTML**
MHTML combine le HTML normal avec des ressources externes (c'est-à-dire le contenu généralement lié, comme les images, animations, audio, etc.) en un seul fichier. Il est utilisé pour les courriels avec l'extension de fichier .mht. Aspose.Cells prend en charge la lecture et l'écriture des fichiers MHTML.

L'exemple de code ci-dessous montre comment enregistrer un classeur en tant que fichier MHTML en utilisant C++ :

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    std::unique_ptr<Workbook> workbook = std::make_unique<Workbook>(inputFilePath);

    // Save file to mhtml format
    U16String outputFilePath(u"out.mht");
    workbook->Save(outputFilePath, SaveFormat::MHtml);

    std::cout << "Workbook saved to MHTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Ajuster automatiquement les colonnes et les lignes lors du chargement du HTML dans le classeur](/cells/fr/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Évitez la notation exponentielle des grands nombres lors de l'importation depuis HTML](/cells/fr/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/)
- [Changer le type de cible de lien HTML](/cells/fr/cpp/change-the-html-link-target-type/)
- [Convertir Excel en HTML avec info-bulle](/cells/fr/cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/fr/cpp/create-transparent-image-of-excel-worksheet/)
- [Supprimer les espaces redondants après un saut de ligne lors de l'importation d'HTML](/cells/fr/cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement en HTML](/cells/fr/cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Désactiver l'exportation des scripts de trame et des propriétés de document](/cells/fr/cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel vers HTML - Utiliser l'option PresentationPreference pour une meilleure mise en page](/cells/fr/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Exclure les styles inutilisés lors de la conversion d'Excel en HTML](/cells/fr/cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Expansion du texte de droite à gauche lors de l'exportation d'un fichier Excel vers HTML](/cells/fr/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Exporter les formatages conditionnels DataBar, ColorScale et IconSet lors de la conversion d'Excel en HTML](/cells/fr/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Exporter les commentaires lors de l'enregistrement d'un fichier Excel en HTML](/cells/fr/cpp/export-comments-while-saving-excel-file-to/)
- [Exporter les propriétés du classeur de document et de la feuille de calcul lors de la conversion d'Excel en HTML](/cells/fr/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Exporter Excel au format HTML avec des lignes de grille](/cells/fr/cpp/export-excel-to-html-with-gridlines/)
- [Exporter la plage de la zone d'impression en HTML](/cells/fr/cpp/export-print-area-range-to/)
- [Exporter un style de bordure similaire lorsque le style de bordure n'est pas pris en charge par les navigateurs Web](/cells/fr/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Exporter la feuille de calcul CSS séparément dans le HTML de sortie](/cells/fr/cpp/export-worksheet-css-separately-in-output/)
- [Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement au format HTML](/cells/fr/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Préfixer les styles des éléments de table avec la propriété HtmlSaveOptions.TableCssId](/cells/fr/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Empêcher l'exportation du contenu masqué de la feuille de calcul lors de l'enregistrement au format HTML](/cells/fr/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Reconnaître les balises auto-fermantes](/cells/fr/cpp/recognise-self-closing-tags/)
- [Rendre le remplissage dégradé pour WordArt lors de la conversion des feuilles de calcul en HTML](/cells/fr/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Définir la largeur de colonne sur une unité extensible comme em ou pourcentage](/cells/fr/cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Définir la police par défaut lors du rendu de la feuille de calcul en HTML](/cells/fr/cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Spécifier comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType](/cells/fr/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Prise en charge de la mise en page des balises DIV lors du chargement d'HTML dans le classeur Excel](/cells/fr/cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)
- [Activer les propriétés personnalisées CSS lors de l'enregistrement en HTML](/cells/fr/cpp/enable-css-custom-properties-while-saving-to-html/)
{{< app/cells/assistant language="cpp" >}}
