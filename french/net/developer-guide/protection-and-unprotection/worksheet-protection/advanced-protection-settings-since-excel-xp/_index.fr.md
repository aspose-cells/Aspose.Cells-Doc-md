---
title: Paramètres de protection avancée depuis Excel XP
type: docs
weight: 30
url: /fr/net/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

Depuis la publication d'Excel 2002 ou XP, Microsoft a ajouté de nombreux paramètres de protection avancés.

{{% /alert %}}

## **Introduction**

Ces paramètres de protection restreignent ou permettent aux utilisateurs de:

- Supprimer des lignes ou des colonnes.
- Modifier le contenu, les objets ou les scénarios.
- Formater les cellules, les lignes ou les colonnes.
- Insérer des lignes, des colonnes ou des hyperliens.
- Sélectionner des cellules verrouillées ou déverrouillées.
- Utiliser des tableaux croisés dynamiques et bien plus encore.

Aspose.Cells prend en charge tous les paramètres de protection avancés offerts par Excel XP ou les versions ultérieures.

### **Paramètres de protection avancés utilisant Excel XP et les versions ultérieures**

Pour afficher les paramètres de protection disponibles dans Excel XP :

1. Dans le menu **Outils**, sélectionnez **Protection** puis **Protéger la feuille**. Une boîte de dialogue s'affiche.

Pour afficher les paramètres de protection disponibles dans Excel 2016

1. Dans le menu **Fichier**, sélectionnez **Protéger le classeur** puis **Protéger la feuille en cours**.
1. Sélectionnez **Protéger la feuille** dans le menu **Révision**.

Suivre les étapes mentionnées ci-dessus affichera une boîte de dialogue où vous pourrez autoriser ou restreindre les fonctionnalités des feuilles de calcul ou appliquer un mot de passe à la feuille de calcul.

### **Paramètres de protection avancés utilisant Aspose.Cells**

Aspose.Cells prend en charge tous les paramètres de protection avancés.

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit la propriété [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) qui est utilisée pour appliquer ces paramètres de protection avancés. La propriété [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) est en fait un objet de la classe [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) qui encapsule plusieurs propriétés booléennes pour désactiver ou activer des restrictions.

Voici un petit exemple d'application. Il ouvre un fichier Excel et utilise la plupart des paramètres de protection avancés pris en charge par Excel XP et les versions ultérieures.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

Veuillez ne pas appeler la méthode [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) lors de l'utilisation de la propriété [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection). Enregistrez également le fichier au format Excel97To2003 ou Xlsx car les paramètres de protection avancés sont uniquement pris en charge par Excel XP et les versions ultérieures.

{{% /alert %}}

### **Problème de verrouillage de cellules**

Si vous souhaitez empêcher les utilisateurs de modifier des cellules, les cellules doivent être verrouillées avant d'appliquer des paramètres de protection. Sinon, les cellules peuvent être modifiées même si la feuille de calcul est protégée. Dans Microsoft Excel XP, les cellules peuvent être verrouillées via la boîte de dialogue suivante:

|**Boîte de dialogue pour verrouiller les cellules dans Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Il est possible de verrouiller des cellules en utilisant l'API Aspose.Cells également. Chaque cellule peut obtenir un formatage qui contient une propriété booléenne, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Définissez la propriété [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) sur **true** ou **false** pour verrouiller ou déverrouiller la cellule.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
