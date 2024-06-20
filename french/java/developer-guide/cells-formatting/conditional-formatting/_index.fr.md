---
title: Formatage conditionnel
type: docs
weight: 120
url: /fr/java/conditional-formatting/
---

{{% alert color="primary" %}} 

Le formatage conditionnel est une fonctionnalité avancée de Microsoft Excel qui vous permet d'appliquer des formats à une cellule ou à une plage de cellules et de modifier ce format en fonction de la valeur de la cellule ou de la valeur d'une formule. Par exemple, une cellule peut apparaître en gras seulement lorsque la valeur de la cellule est supérieure à 500. Lorsque la valeur de la cellule satisfait à la condition, le format spécifié est appliqué à la cellule. Si la valeur de la cellule ne satisfait pas à la condition, la mise en forme par défaut est utilisée. Dans Microsoft Excel, sélectionnez **Format**, puis **Formatage conditionnel** pour ouvrir la boîte de dialogue Formatage conditionnel.

**Formatage conditionnel dans Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_1.png)

Aspose.Cells prend en charge l'application du formatage conditionnel aux cellules en cours d'exécution. Cet article explique comment faire.

{{% /alert %}} 
## **Application de la mise en forme conditionnelle**
Aspose.Cells prend en charge la mise en forme conditionnelle de deux manières :

- [Utiliser une feuille de calcul créée avec le concepteur](/cells/fr/java/conditional-formatting/).
- [Créer une mise en forme conditionnelle à l'exécution](/cells/fr/java/conditional-formatting/).
### **Utilisation de la feuille de calcul du concepteur**
Les développeurs peuvent créer une feuille de calcul créée avec le concepteur qui contient une mise en forme conditionnelle dans Microsoft Excel, puis ouvrir cette feuille de calcul avec Aspose.Cells. Aspose.Cells charge et enregistre la feuille de calcul créée avec le concepteur, en conservant tous les paramètres de mise en forme conditionnelle. Pour en savoir plus sur les feuilles de calcul créées avec le concepteur, consultez [Qu'est-ce qu'une feuille de calcul créée avec le concepteur](/cells/fr/java/what-is-a-designer-spreadsheet/).
## **Application de la mise en forme conditionnelle à l'exécution**
Aspose.Cells prend en charge l'application de la mise en forme conditionnelle à l'exécution.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConditionalFormattingatRuntime-ConditionalFormattingatRuntime.java" >}}
### **Définir la police**
**Définir les polices dans Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontStyle-SettingFontStyle.java" >}}
### **Définir la bordure**
**Définir les bordures dans Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetBorder-SetBorder.java" >}}
### **Définir le motif**
**Définir un motif de cellule dans Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetPattern-SetPattern.java" >}}

## **Sujets avancés**
- [Ajouter un ensemble d'icônes conditionnelles avec le texte de la cellule](/cells/fr/java/add-conditional-icons-set-with-the-cell-text/)
- [Ajout de mises en forme conditionnelles à 2 couleurs et à 3 couleurs](/cells/fr/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Appliquer une mise en forme conditionnelle dans les feuilles de calcul](/cells/fr/java/apply-conditional-formatting-in-worksheets/)
- [Appliquer un ombrage aux lignes et colonnes alternées avec une mise en forme conditionnelle](/cells/fr/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)

