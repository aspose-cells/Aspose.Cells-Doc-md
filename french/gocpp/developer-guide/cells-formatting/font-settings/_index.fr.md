---
title: Paramètres de police avec Golang via C++
linktitle: Paramètres de la police
type: docs
weight: 30
url: /fr/go-cpp/cells-font-settings/
description: Aspose.Cells est une bibliothèque C++ pour le travail avec des fichiers de tableur. Elle supporte la configuration des paramètres de police des cellules, permettant aux utilisateurs de personnaliser le style et les propriétés de la police des cellules. Cet article montre comment utiliser la bibliothèque Aspose.Cells pour définir les paramètres de police des cellules.
keywords: Aspose.Cells, Cellules, Paramètres de police, Styles, Propriétés
---

{{% alert color="primary" %}}

L'apparence d'un texte peut être contrôlée en modifiant les paramètres de police. Ces paramètres incluent le nom, le style, la taille, la couleur et d'autres effets de la police. Comme Microsoft Excel, Aspose.Cells supporte la configuration des paramètres de police des cellules.

{{% /alert %}}

## **Configuration des paramètres de police**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Chaque élément de la collection [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells fournit les méthodes [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) et [**SetStyle**](https://reference.aspose.com/cells/go-cpp/cell/setstyle/) de la classe [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) utilisées pour obtenir et définir le style de mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) fournit des propriétés pour configurer les paramètres de police.

### **Définition du nom de la police**

Les développeurs peuvent appliquer n'importe quelle police au texte d'une cellule en utilisant la propriété [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings.go" >}}
### **Définition du style de police en gras**

Les développeurs peuvent mettre en gras le texte en définissant la propriété [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) sur **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-1.go" >}}
### **Définition de la taille de police**

Définissez la taille de la police avec la propriété [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-2.go" >}}
### **Définition de la couleur de police**

Utilisez la propriété [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) pour définir la couleur de la police. Sélectionnez n'importe quelle couleur dans l'énumération Color (faisant partie du framework C++) et assignez-la à la propriété [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-3.go" >}}
### **Définition du type de soulignement de la police**

Utilisez la propriété [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) pour souligner le texte. Aspose.Cells propose divers types de soulignement de police prédéfinis dans l'énumération [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/).

|**Types de soulignement de police**|**Description**|
| :- | :- |
|Accounting|Un soulignement de comptabilité unique|
|Double|Double soulignement|
|DoubleAccounting|Double soulignement de comptabilité|
|None|Pas de soulignement|
|Single|Un seul soulignement|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-4.go" >}}
### **Définition de l'effet Barré**

Appliquer l'effet barré en définissant la propriété [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) à **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-5.go" >}}
### **Définir l'effet de bas indice**

Appliquer le bas indice en définissant la propriété [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) à **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-6.go" >}}
### **Définition de l'effet exposant sur la police**

Les développeurs peuvent appliquer l'effet exposant sur la police en définissant la propriété [**IsSuperscript**](https://reference.aspose.com/cells/go-cpp/font/issuperscript/) de l'objet [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) à **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-7.go" >}}
## **Sujets avancés**
- [Appliquer les effets exposant et bas indice sur les polices](/cells/fr/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur](/cells/fr/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
