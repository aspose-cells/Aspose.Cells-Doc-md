---
title: Ajout de la protection Cell dans la feuille de calcul
type: docs
weight: 130
url: /fr/net/adding-cell-protection-in-worksheet/
---
{{% alert color="primary" %}} 

Aspose.Cells pour GridDesktop vous permet de protéger vos cellules dans une feuille de calcul. Vous devez d'abord protéger votre feuille de calcul, puis vous pouvez protéger les cellules souhaitées dans une feuille de calcul. Afin de protéger la feuille de calcul, veuillez définir**Feuille de calcul.Protégé** propriété sur true, puis utilisez**Feuille de calcul.SetProtected()** méthode pour protéger la plage de cellules.

{{% /alert %}} 
## **Protégez Cell en utilisant Aspose.Cells.GridDesktop**
 L'exemple de code suivant protège toutes les cellules de la plage**A1:B1** de la feuille de calcul active de GridDesktop. Lorsque vous double-cliquez sur une cellule de cette plage, vous ne pourrez pas modifier. Cela rendra ces cellules en lecture seule.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
