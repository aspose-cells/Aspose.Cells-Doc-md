---
title: Travailler avec les événements de double clic de GridWeb
type: docs
weight: 80
url: /fr/net/aspose-cells-gridweb/gridweb-double-click-event/
keywords: GridWeb, double clic, événement, clic
description: Cet article présente comment utiliser l événement de double clic dans GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb contient trois types d'événements de double clic :

- CellDoubleClick, déclenché lorsqu'une cellule est double-cliquée.
- ColumnDoubleClick, déclenché lorsque l'en-tête de colonne est double-cliqué.
- RowDoubleClick, déclenché lorsque l'en-tête de ligne est double-cliqué.

Ce sujet traite de l'activation des événements de double clic dans Aspose.Cells.GridWeb. Il traite également de la création de gestionnaires d'événements pour ces événements.|

{{% /alert %}} 
## **Activation des événements de double clic**
Tous les types d'événements de double clic peuvent être activés côté client en définissant la propriété EnableDoubleClickEvent du contrôle GridWeb sur true.

{{% alert color="primary" %}} 

Par défaut, la propriété EnableDoubleClickEvent est définie sur false. Cela signifie que les événements de double clic ne sont pas activés par défaut. Pour implémenter de tels événements, activez d'abord la fonctionnalité.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



Une fois les événements de double clic activés, il est possible de créer des gestionnaires d'événements pour n'importe quel événement de double clic. Ces gestionnaires d'événements effectuent des tâches spécifiques lorsqu'un événement de double clic donné est déclenché.|
## **Gestion des événements de double clic**
Pour créer un gestionnaire d'événements dans Visual Studio :

1. Double-cliquez sur un événement dans la liste des **Événements** dans le volet Propriétés.

Dans cet exemple, nous avons implémenté des gestionnaires d'événements pour divers événements de double-clic.
### **Double Clic Cell**
Le gestionnaire d'événements pour l'événement CellDoubleClick fournit un argument de type CellEventArgs, qui fournit les informations complètes de la cellule sur laquelle un double-clic a été fait.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Double Clic sur l'en-tête de colonne**
Le gestionnaire d'événements pour l'événement ColumnDoubleClick fournit un argument de type RowColumnEventArgs qui fournit le numéro d'index de la colonne pour l'en-tête qui a été double-cliqué ainsi que d'autres informations.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Double Clic sur l'en-tête de ligne**
Le gestionnaire d'événements pour l'événement RowDoubleClick fournit un argument de type RowColumnEventArgs qui fournit le numéro d'index de la ligne pour l'en-tête qui a été double-cliqué ainsi que d'autres informations connexes.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
