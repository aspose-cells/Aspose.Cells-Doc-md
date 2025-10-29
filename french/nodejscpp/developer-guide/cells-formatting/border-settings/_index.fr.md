---  
title: Paramètres de bordure
linktitle: Paramètres de bordure  
description: Comment utiliser la bibliothèque Aspose.Cells dans Node.js via C++ pour définir le style de bordure et la couleur des cellules. En ajustant la largeur, le style et la couleur de la bordure, vous avez plus de contrôle sur l apparence des cellules.  
keywords: Aspose.Cells, Paramètres de Bordure de Cellule, Node.js via C++, Largeur de la Bordure, Style de la Bordure, Couleur de la Bordure  
type: docs  
weight: 40  
url: /fr/nodejs-cpp/cells-border-settings/  
---  

## **Ajout de bordures aux cellules**  

Microsoft Excel permet aux utilisateurs de formater les cellules en ajoutant des bordures. Le type de bordure dépend de l'endroit où elle est ajoutée. Par exemple, une bordure supérieure est celle ajoutée en haut d'une cellule. Les utilisateurs peuvent également modifier le style de ligne et la couleur des bordures.  

Avec Aspose.Cells for Node.js via C++, les développeurs peuvent ajouter des bordures et personnaliser leur apparence de la même manière flexible que dans Microsoft Excel.  

### **Ajout de bordures aux cellules**  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit la collection [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Chaque élément dans la collection [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Aspose.Cells fournit la méthode [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) dans la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). La méthode [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) est utilisée pour définir le style de mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) fournit des propriétés pour ajouter des bordures aux cellules.  

#### **Ajout de bordures à une cellule**  

Les développeurs peuvent ajouter des bordures à une cellule en utilisant la collection [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Le type de bordure est passé comme un index à la collection [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--). Tous les types de bordures sont prédéfinis dans l'énumération [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype).  

**Énumération de bordure**  

|**Types de bordures**|**Description**|  
| :- | :- |  
|BottomBorder|Une ligne de bordure inférieure|  
|DiagonalDown|Une ligne diagonale de haut gauche à bas droite|  
|DiagonalUp|Une ligne diagonale de bas gauche à haut droit|  
|LeftBorder|Une ligne de bordure gauche|  
|RightBorder|Une ligne de bordure droite|  
|TopBorder|Une ligne de bordure supérieure|  

La collection [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) stocke toutes les bordures. Chaque bordure dans la collection [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) est représentée par un objet [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border) qui fournit deux propriétés, [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/border/#setColor-color-) et [**setLineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) pour définir respectivement la couleur et le style de la ligne d'une bordure.  

Pour définir la couleur de la ligne d'une bordure, choisissez une couleur en utilisant l'énumération Color (partie de Node.js) et assignez-la à la propriété color de l'objet Border.  

Le style de ligne de la bordure est défini en sélectionnant un style de ligne dans l'énumération [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype).  

**Énumération de Type de Bordure Cellulaire**  

|**Styles de ligne**|**Description**|  
| :- | :- |  
|DashDot|Ligne pointillée fine|  
|DashDotDot|Ligne pointillée fine avec point|  
|Dashed|Ligne en tirets|  
|Dotted|Ligne en pointillés|  
|Double|Ligne double|  
|Hair|Ligne fine|  
|MediumDashDot|Ligne mixte pointillée|  
|MediumDashDotDot|Ligne mixte pointillée-traitée|  
|MediumDashed|Ligne en pointillés moyens|  
|None|Aucune ligne|  
|Medium|Ligne moyenne|  
|SlantedDashDot|Ligne mixte pointillée inclinée moyenne|  
|Thick|Ligne épaisse|  
|Thin|Ligne fine|  
Sélectionnez l'un des styles de ligne, puis assignez-le à la propriété [**lineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) de l'objet [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToCell.js" >}}

{{% alert color="primary" %}}  
Vous devez définir à la fois le style de ligne et la couleur en même temps. Les deux lignes diagonales de la bordure doivent avoir le même style de ligne et la même couleur.  
{{% /alert %}}  

#### **Ajout de bordures à une plage de cellules**  

Il est également possible d'ajouter des bordures à une plage de cellules plutôt qu'à une seule cellule. Pour ce faire, créez d'abord une plage de cellules en appelant la méthode [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) de la collection [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Elle prend les paramètres suivants :  

- Première ligne, la première ligne de la plage.  
- Première colonne, represente la première colonne de la plage.  
- Nombre de lignes, le nombre de lignes dans la plage.  
- Nombre de colonnes, le nombre de colonnes dans la plage.  

La méthode [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) renvoie un objet [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range), qui contient la plage de cellules spécifiée. L'objet [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) fournit une méthode [**setOutlineBorder**](https://reference.aspose.com/cells/nodejs-cpp/range/#setOutlineBorder-bordertype-cellbordertype-cellscolor-) qui accepte les paramètres suivants pour ajouter une bordure à cette plage de cellules :  

- **Type de Bordure**, le type de bordure, sélectionné dans l'énumération [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype).  
- **Style de Ligne**, le style de ligne de la bordure, sélectionné dans l'énumération [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype).  
- **Couleur**, la couleur de la ligne, sélectionnée dans l'énumération Color.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToRange.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
