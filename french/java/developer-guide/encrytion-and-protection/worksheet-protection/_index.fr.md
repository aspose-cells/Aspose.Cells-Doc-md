---
title: Protéger et déprotéger la feuille de calcul
type: docs
weight: 50
url: /fr/java/protect-and-unprotect-worksheet/
---

## **Protéger les feuilles de calcul**

Lorsqu'une feuille de calcul est protégée, les actions qu'un utilisateur peut effectuer sont restreintes. Par exemple, ils ne peuvent pas saisir de données, insérer ou supprimer des lignes ou des colonnes, etc. Les options de protection générales dans Microsoft Excel sont :

- Contenu
- Objets
- Scénarios

Les feuilles de calcul protégées ne cachent ni ne protègent les données sensibles, c'est donc différent du chiffrement de fichier. Généralement, la protection de la feuille de calcul convient à des fins de présentation. Elle empêche l'utilisateur final de modifier les données, le contenu et la mise en forme dans la feuille de calcul.

### **Ajout ou suppression de protection**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe Workbook contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La classe Worksheet fournit la méthode [**Protect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)) qui est utilisée pour appliquer une protection à une feuille de calcul. La méthode Protect accepte les paramètres suivants :

- Type de protection, le type de protection à appliquer sur la feuille de calcul. Le type de protection est appliqué à l'aide de l'énumération [**ProtectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType).
- Nouveau mot de passe, le nouveau mot de passe utilisé pour protéger la feuille de calcul.
- Ancien mot de passe, l'ancien mot de passe, si la feuille de calcul est déjà protégée par mot de passe. Si la feuille de calcul n'est pas déjà protégée, il suffit de transmettre une valeur nulle.

L'énumération ProtectionType contient les types de protection prédéfinis suivants :

|**Types de protection**|**Description**|
| :- | :- |
|[**ALL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|L'utilisateur ne peut rien modifier sur cette feuille de calcul|
|[**CONTENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|L'utilisateur ne peut pas saisir de données dans cette feuille de calcul|
|[**OBJECTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|L'utilisateur ne peut pas modifier les objets graphiques|
|[**SCENARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|L'utilisateur ne peut pas modifier les scénarios enregistrés|
|[**STRUCTURE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|L'utilisateur ne peut pas modifier la structure enregistrée|
|[**WINDOWS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|L'utilisateur ne peut pas modifier les fenêtres enregistrées|
|[**NONE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Aucune protection|

L'exemple ci-dessous montre comment protéger une feuille de calcul avec un mot de passe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

Après que le code ci-dessus a été utilisé pour protéger la feuille de calcul, vérifiez la protection sur la feuille de calcul en l'ouvrant. Une fois que vous ouvrez le fichier et essayez d'ajouter des données à la feuille de calcul, la boîte de dialogue suivante s'affiche :

**Une boîte de dialogue avertissant qu'un utilisateur ne peut pas modifier la feuille de calcul** 

![todo:image_alt_text](protect-and-unprotect-worksheet_1.png)

Pour travailler sur la feuille de calcul, déprotégez la feuille de calcul en sélectionnant la **Protection**, puis **Déprotéger la feuille** dans le menu **Outils** comme indiqué ci-dessous.

**Sélection de l'option Déprotéger la feuille** 

![todo:image_alt_text](protect-and-unprotect-worksheet_2.png)

Une boîte de dialogue s'ouvre demandant un mot de passe.

**Saisir le mot de passe pour désactiver la protection de la feuille de calcul** 

![todo:image_alt_text](protect-and-unprotect-worksheet_3.png)

### **Protection de quelques cellules**

Il peut y avoir certains scénarios où vous avez besoin de verrouiller uniquement quelques cellules dans la feuille de calcul. Si vous voulez verrouiller certaines cellules spécifiques dans la feuille de calcul, vous devez déverrouiller toutes les autres cellules de la feuille. Toutes les cellules d'une feuille de calcul sont déjà initialisées pour le verrouillage, vous pouvez vérifier ceci en ouvrant un fichier Excel dans MS Excel et en cliquant sur **Format | Cellules...** pour afficher la boîte de dialogue **Format Cells** puis cliquez sur l'onglet Protection et voir si une case à cocher intitulée "Verrouillée" est cochée par défaut.

Voici les deux approches pour implémenter la tâche.

**Méthode 1 :**

Les points suivants décrivent comment verrouiller quelques cellules à l'aide de MS Excel. Cette méthode s'applique aux versions Microsoft Office Excel 97, 2000, 2002, 2003 et supérieures.

1. Sélectionnez la feuille de calcul entière en cliquant sur le bouton Tout sélectionner (le rectangle gris directement au-dessus du numéro de ligne pour la ligne 1 et à gauche de la lettre de colonne A).
1. Cliquez sur Cellules dans le menu Format, cliquez sur l'onglet Protection, puis désélectionnez la case à cocher Verrouillée.

   Cela déverrouille toutes les cellules de la feuille de calcul

{{% alert color="primary" %}}

Si la commande des cellules n'est pas disponible, des parties de la feuille de calcul peuvent déjà être verrouillées. Dans le menu Outils, pointez sur Protection, puis cliquez sur Désactiver la feuille.

{{% /alert %}}

1. Sélectionnez simplement les cellules que vous voulez verrouiller et répétez l'étape 2, mais cette fois, sélectionnez la case à cocher Verrouillée.
1. Dans le menu **Outils**, sélectionnez **Protection**, cliquez sur **Protéger la feuille**, puis cliquez sur **OK**.

{{% alert color="primary" %}}

Dans la boîte de dialogue Protéger la feuille, vous avez la possibilité de spécifier un mot de passe et de sélectionner les éléments que vous voulez que les utilisateurs puissent modifier.

{{% /alert %}}

**Méthode2 :**

Dans cette méthode, nous utilisons uniquement l'API Aspose.Cells pour effectuer la tâche.

L'exemple suivant montre comment protéger quelques cellules dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille 3 cellules (A1, B1, C1) dans celle-ci. Enfin, il protège la feuille de calcul. Une ligne / colonne a une API de style qui contient également une méthode setLocked. Vous pouvez utiliser cette méthode pour verrouiller ou déverrouiller la ligne / colonne.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Protéger une ligne dans la feuille de calcul**

Aspose.Cells vous permet de verrouiller facilement une ligne dans la feuille de calcul. Ici, nous pouvons utiliser la méthode [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) de la classe [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) pour appliquer un style à une ligne particulière dans la feuille de calcul. Cette méthode prend deux arguments : un objet [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) et une structure [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) qui contient tous les membres liés à la mise en forme appliquée.

L'exemple suivant montre comment protéger une rangée dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille la première rangée dans celle-ci. Enfin, il protège la feuille de calcul. Une ligne / colonne a une API de style qui contient également une méthode setCellLocked. Vous pouvez verrouiller ou déverrouiller la ligne / colonne en utilisant la structure StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Protéger une colonne dans la feuille de calcul**

Aspose.Cells vous permet de verrouiller facilement une colonne dans la feuille de calcul. Ici, nous pouvons utiliser la méthode [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) de la classe [**Column**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) pour appliquer un style à une colonne particulière dans la feuille de calcul. Cette méthode prend deux arguments : un objet [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) et une structure [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) qui contient tous les membres liés à la mise en forme appliquée.

L'exemple suivant montre comment protéger une colonne dans la feuille de calcul. Il déverrouille d'abord toutes les cellules de la feuille de calcul, puis verrouille la première colonne dans celle-ci. Enfin, il protège la feuuille de calcul. Une ligne / colonne a une API de style qui contient également une méthode setLocked. Vous pouvez verrouiller ou déverrouiller la ligne / colonne en utilisant la structure StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Déprotéger une feuille de calcul**

[Protection des feuilles de calcul](/cells/fr/java/protéger-et-désactiver-la-feuille-de-calcul/#protéger-les-feuilles-de-calcul) et [Paramètres de protection avancés depuis Excel XP](/cells/fr/java/protéger-et-désactiver-la-feuille-de-calcul/#paramètres-de-protection-avancés-depuis-excel-xp) abordent différentes approches pour protéger les feuilles de calcul. Que faire si un développeur doit supprimer la protection d'une feuille de calcul protégée à l'exécution pour apporter des modifications au fichier ? Cela peut facilement être fait avec Aspose.Cells.

### **Utilisation de Microsoft Excel**

Pour supprimer la protection d'une feuille de calcul:

Dans le menu **Outils**, sélectionnez **Protection** puis **Désactiver la protection de la feuille**.

**Sélectionner Désactiver la protection de la feuille** 

![todo:image_alt_text](protect-and-unprotect-worksheet_4.png)

La protection est supprimée, sauf si la feuille de calcul est protégée par mot de passe. Dans ce cas, une boîte de dialogue demande le mot de passe.

**Saisir le mot de passe pour désactiver la protection de la feuille de calcul** 

![todo:image_alt_text](protect-and-unprotect-worksheet_5.png)

### **Utilisation d'Aspose.Cells**

Une feuille de calcul peut être désactivée en appelant la méthode [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La méthode [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--) peut être utilisée de deux manières, décrites ci-dessous.

### **Désactiver une feuille de calcul simplement protégée**

Une feuille de calcul simplement protégée est une feuille non protégée par un mot de passe. De telles feuilles de calcul peuvent être désactivées en appelant la méthode de désactivation sans passer de paramètre.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Désactiver une feuille de calcul protégée par mot de passe**

Une feuille de calcul protégée par mot de passe est une feuille protégée par un mot de passe. De telles feuilles de calcul peuvent être désactivées en appelant une version surchargée de la méthode de désactivation qui prend le mot de passe en tant que paramètre.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Paramètres de protection avancés depuis Excel XP**

[Protection des feuilles de calcul](/cells/fr/java/protect-and-unprotect-worksheet/#protect-worksheets) abordant la protection d'une feuille de calcul dans Microsoft Excel 97 et 2000. Mais depuis la version Excel 2002 ou XP, Microsoft a ajouté de nombreux paramètres de protection avancés. Ces paramètres de protection restreignent ou autorisent les utilisateurs à :

- Supprimer des lignes ou des colonnes.
- Modifier le contenu, les objets ou les scénarios.
- Formater les cellules, les lignes ou les colonnes.
- Insérer des lignes, des colonnes ou des hyperliens.
- Sélectionner des cellules verrouillées ou déverrouillées.
- Utiliser des tableaux croisés dynamiques et bien plus encore.

Aspose.Cells prend en charge tous les paramètres de protection avancés offerts par Excel XP et les versions ultérieures.

### **Paramètres de protection avancés utilisant Excel XP et les versions ultérieures**

Pour afficher les paramètres de protection disponibles dans Excel XP :

1. Dans le menu **Outils**, sélectionnez **Protection** suivi de **Protéger la feuille**.
   Une boîte de dialogue s'affiche.

   **Boîte de dialogue pour afficher les options de protection dans Excel XP**

![todo:image_alt_text](protect-and-unprotect-worksheet_6.png)

1. Autoriser ou restreindre les fonctionnalités des feuilles de calcul ou appliquer un mot de passe.

### **Paramètres de protection avancés utilisant Aspose.Cells**

Aspose.Cells supporte tous les paramètres de protection avancés.

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe Workbook contient une collection WorksheetCollection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La classe Worksheet fournit la propriété Protection qui est utilisée pour appliquer ces paramètres de protection avancés. La propriété Protection est en fait un objet de la classe [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) qui encapsule plusieurs propriétés booléennes pour désactiver ou activer des restrictions.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

Voici un petit exemple d'application. Il ouvre un fichier Excel et utilise la plupart des paramètres de protection avancés pris en charge par Excel XP et les versions ultérieures.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Enregistrez le fichier au format EXCEL97TO2003 ou XLSX car ces paramètres de protection avancés ne sont pris en charge que par MS Excel XP et les versions ultérieures.

{{% /alert %}}

### **Problème de verrouillage de cellules**

Si vous souhaitez empêcher les utilisateurs de modifier des cellules, les cellules doivent être verrouillées avant d'appliquer des paramètres de protection. Sinon, les cellules peuvent être modifiées même si la feuille de calcul est protégée. Dans Microsoft Excel XP, les cellules peuvent être verrouillées à l'aide de la boîte de dialogue suivante :

**Boîte de dialogue pour verrouiller les cellules dans Excel XP** 

![todo:image_alt_text](protect-and-unprotect-worksheet_7.png)

Il est possible de verrouiller des cellules en utilisant l'API Aspose.Cells également. Chaque cellule possède une API Style qui contient de plus une méthode setLocked. Utilisez-la pour verrouiller ou déverrouiller des cellules.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
