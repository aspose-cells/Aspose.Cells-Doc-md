---
title: Déprotéger une feuille de calcul
type: docs
weight: 20
url: /fr/net/unprotect-a-worksheet/
---
{{% alert color="primary" %}}

Si un développeur doit supprimer la protection d'une feuille de calcul protégée lors de l'exécution afin que certaines modifications puissent être apportées au fichier ? Cela peut facilement être fait avec Aspose.Cells.

{{% /alert %}}

## **Déprotéger une feuille de calcul**

### **Utilisation d'Excel Microsoft**

Pour supprimer la protection d'une feuille de calcul :

 Du**Outils** menu, sélectionnez**protection** suivie par**Déprotéger la feuille**. La protection sera supprimée à moins que la feuille de calcul ne soit protégée par un mot de passe. Dans ce cas, une boîte de dialogue demande le mot de passe. Entrez le mot de passe et la feuille de calcul ne sera alors plus protégée.

### **Déprotéger une feuille de calcul simplement protégée à l'aide de Aspose.Cells**

 Une feuille de calcul peut être déprotégée en appelant le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe'[**Déprotéger**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)méthode.
 Une feuille de calcul simplement protégée est une feuille qui n'est pas protégée par un mot de passe. Ces feuilles de calcul peuvent être déprotégées en appelant le[**Déprotéger**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)méthode sans passer de paramètre.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Déprotéger une feuille de travail protégée par mot de passe à l'aide de Aspose.Cells**

Une feuille de calcul protégée par un mot de passe est une feuille protégée par un mot de passe. Ces feuilles de calcul peuvent être déprotégées en appelant une version surchargée du[**Déprotéger**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1)méthode qui prend le mot de passe en paramètre.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
