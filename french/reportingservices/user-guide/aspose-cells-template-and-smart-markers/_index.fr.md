---
title: Modèle Aspose.Cells et repères intelligents
type: docs
weight: 30
url: /fr/reportingservices/aspose-cells-template-and-smart-markers/
---

{{% alert color="primary" %}} 

Un modèle Aspose.Cells est un classeur Microsoft Excel qui contient des repères intelligents. Les repères intelligents servent de marqueurs de données pour les éléments de rapport et sont remplacés par les données correspondantes au moment du rendu. Il existe cinq types de repères intelligents, répertoriés ci-dessous. Tous les repères peuvent être insérés dans un modèle par Aspose.Cells.Report.Designer. Ils peuvent également être édités manuellement. 

{{% /alert %}} 
### **Marqueurs intelligents**
#### **Repères de données**
Le format des **repères de données** est &=NomEnsembleDeDonnées.NomChamp. Par exemple : &=DétailVentes.ventes où DétailVentes est le nom d'un ensemble de données ou d'une requête et ventes est le nom de l'un de ses champs. Au moment du rendu, les repères de données sont remplacés par les valeurs de l'ensemble de données fournies par Reporting Services.
#### **Repères de formules de Reporting Services**
Le format des **repères de formules de Reporting Services** est &=expression. Par exemple : &=sum(DétailVentes.ventes)/100. L'expression se compose de fonctions, de champs d'ensemble de données, d'opérateurs, etc. Au moment du rendu, les repères de formules de Reporting Services sont remplacés par des valeurs calculées.
#### **Marqueurs de variables globales des Services de reporting**
Le format des **marqueurs de variables globales** des Services de reporting est &=Globals! Nom de la variable. Par exemple: &=Globals!ExecutionTime où ExecutionTime est le nom d'une variable globale. Les marqueurs de variables globales sont remplacés par les valeurs des variables globales au moment du rendu.
#### **Marqueurs de paramètres des Services de reporting**
Un paramètre de rapport a deux attributs: valeur et étiquette. Par conséquent, les **marqueurs de paramètres** ont deux formats: &= Parameters! NomDuParamètre.Valeur et &=Parameters! NomDuParamètre.Étiquette. Ils indiquent respectivement le nom et l'étiquette du paramètre. Au moment du rendu, les marqueurs de paramètres sont remplacés par les valeurs de paramètre entrées par l'utilisateur.
#### **Formules dynamiques**
Pour effectuer des calculs sur les lignes insérées, utilisez des formules dynamiques. Les **formules dynamiques** vous permettent d'insérer des formules Microsoft Excel dans des cellules même lorsque la formule fait référence à des lignes qui seront insérées lors du processus d'exportation. Elles peuvent être répétées pour chaque ligne insérée ou utilisées uniquement avec des cellules où des marqueurs de données sont placés pour elles.

Le format des formules dynamiques est &=&=RépéterFormuleDynamique.

Les formules dynamiques permettent les options supplémentaires suivantes:

- {r} – Numéro de ligne actuelle.
- {2}, {-1} – Décalage par rapport au numéro de ligne actuelle.

**Une formule dynamique répétée et la feuille de calcul Excel résultante** 

![todo:image_alt_text](aspose-cells-template-and-smart-markers_1.png)
