---
title: Sous-rapports
type: docs
weight: 20
url: /fr/reportingservices/sub-reports/
---
{{% alert color="primary" %}} 

Nous avons intégré la prise en charge de l'intégration d'un sous-rapport dans une ligne de groupe de tableaux. Le format est :

&=subreport{ReportName=le nom de votre rapport ; nom du paramètre1 = valeur du paramètre1 ; nom du paramètre2 = valeur du paramètre2 ;......} 

{{% /alert %}} 
### **Exemple**
**Un sous-rapport dans un tableau** 

![tâche : image_autre_texte](sub-reports_1.png)

 Dans l'exemple, le nom du sous-rapport est "Sales Order Detail". Il a un paramètre,*Numéro de commande* . La valeur du paramètre est*EmpSalesDetail.SalesOrderNumber.*
#### **Restrictions sur l'utilisation des sous-rapports**
- Le sous-rapport doit être conçu avec l'outil Aspose.Cells.Reporting Services Designer.
- Le sous-rapport ne peut être intégré que dans la ligne du groupe de tableaux et la ligne du groupe ne peut pas contenir d'autres éléments que le sous-rapport. L'intégration d'un sous-rapport dans les lignes de détail du tableau ou les lignes de pied de page n'est pas autorisée.
- Actuellement, l'imbrication de plusieurs niveaux n'est pas prise en charge. Le sous-rapport ne peut pas contenir de rapport intégré.
