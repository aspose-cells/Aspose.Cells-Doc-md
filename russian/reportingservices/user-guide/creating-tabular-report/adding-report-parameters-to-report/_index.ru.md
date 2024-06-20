---
title: Добавление параметров отчета к отчету
type: docs
weight: 60
url: /ru/reportingservices/adding-report-parameters-to-report/
---

{{% alert color="primary" %}} 

Шаблон отчета Aspose.Cells поддерживает параметры отчета Reporting Services в качестве источника данных для ячеек, которые содержат маркер параметра Reporting Services. Пожалуйста, обратитесь к [Шаблону и умным маркерам Aspose.Cells](/cells/ru/reportingservices/aspose-cells-template-and-smart-markers/), чтобы узнать о маркерах параметров отчетов Reporting Services. Параметры отчета обычно размещаются в текстовой области заголовка таблицы или нижнего колонтитула.

{{% /alert %}} 
### **Добавление параметра отчета**
Чтобы добавить параметры отчета к отчетам:

1. Выберите ячейку. 

   **Выбор ячейки** 

![todo:image_alt_text](adding-report-parameters-to-report_1.png)




1. Нажмите Вставить формулу на панели инструментов Aspose.Cells.Report.Designer (

![todo:image_alt_text](adding-report-parameters-to-report_2.png)

).

1. Выберите **Параметры** из панели параметров слева.
   Все параметры перечислены в правой панели. 
1. Выберите параметр, в примере, мы выбрали EmpID.
1. Дважды щелкните по параметру, чтобы выразиться появился в редакторе в верхней части формы.
   У параметра два атрибута данных: метка и значение (атрибут по умолчанию - значение). 

   **Выбор параметра** 

![todo:image_alt_text](adding-report-parameters-to-report_3.png)




1. В образце метка параметра должна быть показана в отчете, поэтому измените выражение на Parameters!EmpID.Label. 

   **Изменение параметра** 

![todo:image_alt_text](adding-report-parameters-to-report_4.png)




1. Нажмите **ОК**.
   Выбранная ячейка содержит маркер параметров отчета. 

   **Параметр отчета, вставленный в ячейку** 

![todo:image_alt_text](adding-report-parameters-to-report_5.png)
