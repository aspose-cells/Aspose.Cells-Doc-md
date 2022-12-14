---
title: Paramètres de protection avancés depuis Excel XP
type: docs
weight: 30
url: /fr/net/advanced-protection-settings-since-excel-xp/
---
{{% alert color="primary" %}}

Depuis la sortie d'Excel 2002 ou XP, Microsoft a ajouté de nombreux paramètres de protection avancés.

{{% /alert %}}

## **Introduction**

Ces paramètres de protection limitent ou autorisent les utilisateurs à :

- Supprimer des lignes ou des colonnes.
- Modifiez des contenus, des objets ou des scénarios.
- Mettre en forme les cellules, les lignes ou les colonnes.
- Insérez des lignes, des colonnes ou des hyperliens.
- Sélectionnez les cellules verrouillées ou déverrouillées.
- Utilisez des tableaux croisés dynamiques et bien plus encore.

Aspose.Cells prend en charge tous les paramètres de protection avancés offerts par Excel XP ou les versions ultérieures.

### **Paramètres de protection avancés à l'aide d'Excel XP et des versions ultérieures**

Pour afficher les paramètres de protection disponibles dans Excel XP :

1.  Du**Outils** menu, sélectionnez**protection** suivie par**Feuille de protection**. Une boîte de dialogue s'affiche.

Pour afficher les paramètres de protection disponibles dans Excel 2016

1.  Du**Dossier** menu, sélectionnez**Protéger le classeur** suivie par**Protéger la feuille actuelle**.
1.  Sélectionnez le**Feuille de protection** dans le**Examen** menu.

En suivant les étapes mentionnées ci-dessus, une boîte de dialogue s'affichera dans laquelle vous pourrez autoriser ou restreindre les fonctionnalités des feuilles de calcul ou appliquer un mot de passe à la feuille de calcul.

### **Paramètres de protection avancés à l'aide de Aspose.Cells**

Aspose.Cells prend en charge tous les paramètres de protection avancés.

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classer.

 La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)la classe fournit la[**protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) propriété utilisée pour appliquer ces paramètres de protection avancés. La[**protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) la propriété est en fait un objet de la[**protection**](https://reference.aspose.com/cells/net/aspose.cells/protection)classe qui encapsule plusieurs propriétés booléennes pour désactiver ou activer des restrictions.

Ci-dessous un petit exemple d'application. Il ouvre un fichier Excel et utilise la plupart des paramètres de protection avancés pris en charge par Excel XP et les versions ultérieures.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

 S'il vous plaît, n'appelez pas le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer'[**Protéger**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) méthode lors de l'utilisation de la[**protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)propriété. Enregistrez également le fichier au format Excel97To2003 ou Xlsx, car les paramètres de protection avancés ne sont pris en charge que par Excel XP et les versions ultérieures.

{{% /alert %}}

### **Cell Problème de verrouillage**

Si vous souhaitez empêcher les utilisateurs de modifier des cellules, les cellules doivent être verrouillées avant que les paramètres de protection ne soient appliqués. Sinon, les cellules peuvent être modifiées même si la feuille de calcul est protégée. Dans Microsoft Excel XP, les cellules peuvent être verrouillées via la boîte de dialogue suivante :

|**Boîte de dialogue pour verrouiller les cellules dans Excel XP**|
|:- |
|![tâche : image_autre_texte](advanced-protection-settings-since-excel-xp_1.png)|

Il est également possible de verrouiller les cellules en utilisant le Aspose.Cells API. Chaque cellule peut recevoir[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) formatage contenant une propriété booléenne,[**Est verrouillé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Met le[**Est verrouillé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) propriété à**vrai** ou**faux** pour verrouiller ou déverrouiller la cellule.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
