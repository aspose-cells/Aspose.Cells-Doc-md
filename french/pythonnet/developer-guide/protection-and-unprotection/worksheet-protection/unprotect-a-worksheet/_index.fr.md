---
title: Déprotéger une feuille de calcul
type: docs
weight: 20
url: /fr/python-net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Si un développeur doit supprimer la protection d’une feuille de calcul protégée en temps d’exécution afin de pouvoir effectuer des modifications sur le fichier, cela peut facilement être réalisé avec Aspose.Cells pour Python via .NET.

{{% /alert %}}

## **Déprotéger une feuille de calcul**

### **Utilisation de Microsoft Excel**

Pour supprimer la protection d'une feuille de calcul:

Dans le menu **Outils**, sélectionnez **Protection** suivi de **Déprotéger la feuille**. La protection sera supprimée sauf si la feuille de calcul est protégée par mot de passe. Dans ce cas, une boîte de dialogue demande le mot de passe. Entrez le mot de passe et la feuille de calcul sera déprotégée alors.

### **Déprotéger une feuille de calcul simplement protégée avec Aspose.Cells pour Python via .NET**

Une feuille de calcul peut être déprotégée en appelant la méthode [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).
Une feuille de calcul simplement protégée est une feuille qui n'est pas protégée par un mot de passe. De telles feuilles peuvent être déprotégées en appelant la méthode [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) sans passer de paramètre.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingSimplyProtectedWorksheet-1.py" >}}

### **Déprotéger une feuille de calcul protégée par mot de passe avec Aspose.Cells pour Python via .NET**

Une feuille de calcul protégée par mot de passe est une feuille protégée par un mot de passe. De telles feuilles peuvent être déprotégées en appelant une version surchargée de la méthode [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/unprotect/) qui prend le mot de passe comme paramètre.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingPasswordProtectedWorksheet-1.py" >}}

