﻿---
title: Formatage des marqueurs intelligents
type: docs
weight: 20
url: /fr/net/formatting-smart-markers/
---
## **Copier l'attribut de style**
Parfois, lorsque vous utilisez des marqueurs intelligents, vous souhaitez copier le style de la cellule qui contient les balises de marqueur intelligent. Vous pouvez utiliser l'attribut CopyStyle des balises du marqueur intelligent à cette fin.
### **Copie de styles à partir de Cells avec des marqueurs intelligents**
 Cet exemple utilise un modèle de fichier Excel simple Microsoft avec deux marqueurs dans les cellules A2 et B2. Le marqueur collé dans la cellule B2 utilise l'attribut CopyStyle, contrairement au marqueur de la cellule A2. Appliquez une mise en forme simple (par exemple, définissez la couleur de la police sur**rouge** et définissez la couleur de remplissage de la cellule sur**jaune**).

Lors de l'exécution du code, Aspose.Cells copie la mise en forme dans tous les enregistrements de la colonne B mais ne conserve pas la mise en forme dans la colonne A.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingCopyStyleAttribute-1.cs" >}}
## **Ajout d'étiquettes personnalisées**
### **Introduction**
Lorsque vous travaillez avec la fonction de regroupement de données de Smart Markers, vous devez parfois ajouter vos propres étiquettes personnalisées à la ligne récapitulative. Vous souhaitez également concaténer le nom de la colonne avec cette étiquette, par exemple "Sous-total des commandes". Aspose.Cells vous fournit les attributs Label et LabelPosition, de sorte que vous pouvez placer vos étiquettes personnalisées dans les marqueurs intelligents tout en concaténant avec les lignes de sous-total dans le regroupement des données.
### **Ajout d'étiquettes personnalisées à concaténer avec les lignes de sous-total dans les marqueurs intelligents**
Cet exemple utilise un[fichier de données](96927971.xlsx) et un[fichier modèle](96927972.xlsx) avec quelques marqueurs dans les cellules. Lors de l'exécution du code, Aspose.Cells ajoute des étiquettes personnalisées aux lignes récapitulatives pour les données groupées.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AddCustomLabels-1.cs" >}}
