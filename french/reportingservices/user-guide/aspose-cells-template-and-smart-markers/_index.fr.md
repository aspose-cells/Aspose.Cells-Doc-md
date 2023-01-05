---
title: Aspose.Cells Modèle et marqueurs intelligents
type: docs
weight: 30
url: /fr/reportingservices/aspose-cells-template-and-smart-markers/
---
{{% alert color="primary" %}} 

 Un modèle Aspose.Cells est un classeur Excel Microsoft qui contient des marqueurs intelligents. Les marqueurs intelligents servent d'espace réservé aux données pour les éléments de rapport et sont remplacés par les données correspondantes au moment du rendu. Il existe cinq types de marqueurs intelligents, répertoriés ci-dessous. Tous les marqueurs peuvent être insérés dans un modèle par Aspose.Cells.Report.Designer. Le peut également être modifié manuellement.

{{% /alert %}} 
### **Marqueurs intelligents**
#### **Marqueurs de données**
 La forme de**marqueurs de données**est &=DataSetName.FieldName. Par exemple : &=SalesDetail.sales où SalesDetail est le nom d'un ensemble de données ou d'une requête et sales est le nom de l'un de ses champs. Au moment du rendu, les marqueurs de données sont remplacés par les valeurs de l'ensemble de données fournies par Reporting Services.
#### **Marqueurs de formules Reporting Services**
 Le format de Reporting Services'**marqueurs de formules** est &=expression. Par exemple : &=sum(SalesDetail.sales)/100. L'expression se compose d'une fonction, de champs d'ensemble de données, d'un opérateur, etc. Au moment du rendu. Les marqueurs de formules Reporting Services sont remplacés par des valeurs calculées.
#### **Marqueurs variables globaux Reporting Services**
 Le format de Reporting Services'**marqueurs de variables globales** est &=Globals ! Nom de variable. Par exemple : &=Globals!ExecutionTime où ExecutionTime est le nom d'une variable globale. Les marqueurs de variables globales sont remplacés par des valeurs de variables globales au moment du rendu.
#### **Marqueurs de paramètres Reporting Services**
Un paramètre de rapport a deux attributs : valeur et étiquette. Par conséquent,**marqueurs de paramètres** ont deux formats : &= Paramètres ! ParamName.Value et &=Paramètres ! ParamName.Label. Ils indiquent respectivement le nom et le libellé du paramètre. Au moment du rendu, les marqueurs de paramètres sont remplacés par les valeurs de paramètre saisies par l'utilisateur.
#### **Formules dynamiques**
 Pour effectuer des calculs sur des lignes insérées, utilisez des formules dynamiques.**Formules dynamiques** vous permet d'insérer Microsoft des formules Excel dans des cellules même lorsqu'une formule fait référence à des lignes qui seront insérées lors du processus d'exportation. Ils peuvent être répétés pour chaque ligne insérée ou utilisés uniquement avec des cellules où des marqueurs de données sont placés pour eux.

Le format des formules dynamiques est &=&=RepeatDynamicFormula.

Les formules dynamiques permettent les options supplémentaires suivantes :

- {r} – Numéro de ligne actuel.
- {2}, {-1} - Décalage par rapport au numéro de ligne actuel.

**Une formule dynamique répétitive et la feuille de calcul Excel qui en résulte** 

![tâche : image_autre_texte](aspose-cells-template-and-smart-markers_1.png)
