---
title: Afficher et masquer les barres de défilement
type: docs
weight: 140
url: /fr/net/display-and-hide-scroll-bars/
---
{{% alert color="primary" %}}

Les barres de défilement sont utiles pour parcourir le contenu de feuilles de calcul larges et profondes, c'est-à-dire comportant de nombreuses lignes et colonnes. La plupart des applications prennent en charge deux types de barre de défilement :

- Barre de défilement verticale
- Barre de défilement horizontale

Ces deux éléments se trouvent dans Microsoft Excel.

Le GridDesktop API de Aspose.Cell fournit des barres de défilement horizontales et verticales pour faire défiler le contenu d'une feuille de calcul. Avec les API Aspose.Cells.GridDesktop, les développeurs peuvent contrôler la visibilité de ces deux barres de défilement.

{{% /alert %}}

## **Contrôle de la visibilité de la barre de défilement**

Pour contrôler la visibilité de la barre de défilement dans GridDesktop, utilisez les propriétés IsVerticalScrollBarVisible et IsHorizontalScrollBarVisible. Les exemples ci-dessous montrent comment masquer et afficher les barres de défilement.

### **Exemples de programmation : masquage des barres de défilement**

Pour masquer les barres de défilement, définissez les propriétés qui contrôlent la visibilité sur false.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-HideScrollbars.cs" >}}

### **Exemples de programmation : rendre les barres de défilement visibles**

Pour rendre les barres de défilement visibles, définissez les propriétés qui contrôlent la visibilité sur true.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-ShowScrollbars.cs" >}}
