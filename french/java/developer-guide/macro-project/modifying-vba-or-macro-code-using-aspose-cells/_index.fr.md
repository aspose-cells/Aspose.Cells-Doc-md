---
title: Modification du code VBA ou macro à l aide d Aspose.Cells
type: docs
weight: 90
url: /fr/java/modifying-vba-or-macro-code-using-aspose-cells/
---

{{% alert color="primary" %}} 

Vous pouvez modifier le code VBA ou macro à l'aide d'Aspose.Cells. Aspose.Cells a ajouté les classes suivantes pour lire et modifier le projet VBA dans le fichier Excel :

- VbaProject
- VbaModuleCollection
- VbaModule

Cet article vous montrera comment modifier le code VBA ou Macro à l'intérieur du fichier Excel source en utilisant Aspose.Cells.

{{% /alert %}} 
## **Exemple**
Le code d'exemple suivant charge le fichier Excel source qui contient un code VBA ou Macro à l'intérieur

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

Après l'exécution du code d'exemple Aspose.Cells, le code VBA ou Macro sera modifié comme ceci

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Vous pouvez télécharger le [fichier Excel source](5472596.xlsm) et le [fichier Excel de sortie](5472597.xlsm) à partir des liens donnés.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






{{< app/cells/assistant language="java" >}}
