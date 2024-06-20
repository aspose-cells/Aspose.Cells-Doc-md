---
title: Sous rapports
type: docs
weight: 20
url: /fr/reportingservices/sub-reports/
---

{{% alert color="primary" %}} 

Nous avons intégré la prise en charge de l'intégration d'un sous-rapport dans une ligne de groupe de table. Le format est :

&=subreport{ReportName=your report name; parameter1 name = parameter1 value; parameter2 name = parameter2 value;......} 

{{% /alert %}} 
### **Exemple**
**Un sous-rapport dans une table** 

![todo:image_alt_text](sub-reports_1.png)

Dans l'exemple, le nom du sous-rapport est "Détail de la commande de vente". Il a un paramètre, *NuméroDeCommandeVente*. La valeur du paramètre est *EmpSalesDetail.SalesOrderNumber.*
#### **Restrictions concernant l'utilisation des sous-rapports**
- Le sous-rapport doit être conçu avec l'outil de conception Aspose.Cells.Reporting Services.
- Le sous-rapport ne peut être intégré que dans la ligne de groupe de table et la ligne de groupe ne peut pas contenir d'autres éléments que le sous-rapport. Il n'est pas autorisé d'intégrer un sous-rapport dans les lignes de détail ou les lignes de pied de table.
- Actuellement, l'imbrication de plus d'un niveau n'est pas prise en charge. Le sous-rapport ne peut contenir de rapport incorporé.
