---  
title: Paramètres de police avec Node.js via C++  
linktitle: Paramètres de la police  
description: Aspose.Cells est une bibliothèque Node.js pour travailler avec des fichiers de feuilles de calcul. Elle supporte la définition des paramètres de police des cellules, permettant aux utilisateurs de personnaliser le style et les propriétés de la police des cellules. Cet article présente comment utiliser la bibliothèque Aspose.Cells pour définir les paramètres de police des cellules.  
keywords: Aspose.Cells, Cellules, Paramètres de police, Styles, Propriétés, Node.js via C++  
type: docs  
weight: 30  
url: /fr/nodejs-cpp/cells-font-settings/  
---  

{{% alert color="primary" %}}  
L'aspect et la sensation d'un texte peuvent être contrôlés en modifiant les paramètres de la police. Les paramètres de police peuvent inclure le nom, le style, la taille, la couleur et d'autres effets des polices. Tout comme Microsoft Excel, Aspose.Cells prend également en charge la configuration des paramètres de police des cellules.  
{{% /alert %}}  

## **Configuration des paramètres de police**  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Aspose.Cells fournit la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) et ses méthodes [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) et [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) qui servent à obtenir et définir le style de mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) offre des propriétés pour configurer les paramètres de police.  

### **Définition du nom de la police**  

Les développeurs peuvent appliquer n'importe quelle police au texte d'une cellule en utilisant la méthode [setName](https://reference.aspose.com/cells/nodejs-cpp/font/#setName-string-) de l'objet [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontName.js" >}}


### **Définition du style de police en gras**  

Les développeurs peuvent rendre le texte en gras en utilisant la méthode [**setIsBold**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsBold-boolean-) de l'objet [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) en la configurant sur **true**.   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetBoldStyle.js" >}}



### **Définition de la taille de police**  

Définissez la taille de la police avec la méthode [**setSize**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSize-number-) de l'objet [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontSize.js" >}}


### **Définition de la couleur de police**  

Utilisez la méthode [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-) de l'objet [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) pour définir la couleur de la police. Sélectionnez une couleur dans l'énumération Couleur (faisant partie de Node.js) et assignez-la à la méthode [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-).   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontColor.js" >}}


### **Définition du type de soulignement de la police**  

Utilisez la méthode [**setUnderline**](https://reference.aspose.com/cells/nodejs-cpp/font/#setUnderline-fontunderlinetype-) de l'objet [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) pour souligner le texte. Aspose.Cells offre divers types de soulignement prédéfinis dans l'énumération [**FontUnderlineType**](https://reference.aspose.com/cells/nodejs-cpp/fontunderlinetype).  

|**Types de soulignement de police**|**Description**|  
| :- | :- |  
|Accounting|Un soulignement de comptabilité unique|  
|Double|Double soulignement|  
|DoubleAccounting|Double soulignement de comptabilité|  
|None|Pas de soulignement|  
|Single|Un seul soulignement|  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontUnderline.js" >}}


### **Définition de l'effet Barré**  

Appliquez le soulignement en définissant la méthode [**setIsStrikeout**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsStrikeout-boolean-) de l'objet [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) sur **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}


### **Définir l'effet de bas indice**  

Appliquez le sous-texte en définissant la méthode [**setIsSubscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSubscript-boolean-) de l'objet [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) sur **true**.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}



### **Définition de l'effet exposant sur la police**  

Les développeurs peuvent appliquer l'effet exposant sur la police en définissant la méthode [**setIsSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSuperscript-boolean-) de l'objet [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) sur **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetSuperscript.js" >}}


## **Sujets avancés**  
- [Appliquer les effets exposant et bas indice sur les polices](/cells/fr/nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur](/cells/fr/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
