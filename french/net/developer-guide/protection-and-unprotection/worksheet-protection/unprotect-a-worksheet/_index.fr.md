---
title: Déprotéger une feuille de calcul
type: docs
weight: 20
url: /fr/net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Si un développeur doit supprimer la protection d'une feuille de calcul protégée pendant l'exécution pour pouvoir apporter des modifications au fichier? Cela peut être facilement fait avec Aspose.Cells.

{{% /alert %}}

## **Déprotéger une feuille de calcul**

### **Utilisation de Microsoft Excel**

Pour supprimer la protection d'une feuille de calcul:

Dans le menu **Outils**, sélectionnez **Protection** suivi de **Déprotéger la feuille**. La protection sera supprimée sauf si la feuille de calcul est protégée par mot de passe. Dans ce cas, une boîte de dialogue demande le mot de passe. Entrez le mot de passe et la feuille de calcul sera déprotégée alors.

### **Déprotéger une feuille de calcul simplement protégée en utilisant Aspose.Cells**

Une feuille de calcul peut être déprotégée en appelant la méthode [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).
Une feuille de calcul simplement protégée est une feuille qui n'est pas protégée par un mot de passe. De telles feuilles peuvent être déprotégées en appelant la méthode [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) sans passer de paramètre.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Déprotéger une feuille de calcul protégée par mot de passe à l'aide d'Aspose.Cells**

Une feuille de calcul protégée par mot de passe est une feuille protégée par un mot de passe. De telles feuilles peuvent être déprotégées en appelant une version surchargée de la méthode [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1) qui prend le mot de passe comme paramètre.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
