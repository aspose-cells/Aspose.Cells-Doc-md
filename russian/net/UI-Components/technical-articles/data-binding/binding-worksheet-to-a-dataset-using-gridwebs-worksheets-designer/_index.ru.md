---
title: Привязка листа к набору данных с использованием конструктора листов GridWeb
type: docs
weight: 20
url: /ru/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset-use-designer/
keywords: GridWeb,bind,DataSet,Designer,designer
description: В этой статье рассматривается способ использования дизайнера Листов для привязки листа к набору данных в GridWeb.
---

{{% alert color="primary" %}} 

Эта статья обсуждает простой подход к привязке листов к таблицам базы данных в режиме GUI с использованием специального инструмента, поставляемого с Aspose.Cells.GridWeb, дизайнером Листов. 

{{% /alert %}} 
## **Привязка листа к базе данных с использованием дизайнера Листов**
	**Шаг 1: Создание образца базы данных**
1. Сначала мы создаем образец базы данных, который будет использоваться в этой статье. Мы используем Microsoft Access для создания базы данных, содержащей таблицу с названием Products. Ее схема показана ниже.
   **Информация о дизайне таблицы Products** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. В таблицу Products добавляется несколько фиктивных записей.
   **Записи в таблице Products** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Шаг 2: Проектирование образцового приложения**
Веб-приложение ASP.NET создано и разработано в Visual Studio.NET, как показано ниже. 
**Проектирование образцового приложения** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Шаг 3: Подключение к базе данных с использованием Server Explorer**
Пришло время подключиться к базе данных. Мы можем легко сделать это, используя Server Explorer в Visual Studio.NET. 

1. Выберите **Data Connection** в **Server Explorer** и щелкните правой кнопкой мыши.
1. Выберите **Add Connection** в меню.
   **Выбор опции Add Connection** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



Отображается диалоговое окно Свойств данных. 
**Диалоговое окно Свойств данных** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



Используя этот диалоговое окно, вы можете подключиться к любой базе данных. По умолчанию он позволяет вам подключаться к базе данных SQL Server. Для этого примера нам нужно подключиться к базе данных Microsoft Access. 

1. Нажмите на вкладку **Поставщик**.
1. Выберите **Microsoft Jet 4.0 OLE DB Provider** из списка **Поставщиков OLE DB(s)**.
1. Нажмите **Далее**.
   **Щелкните Далее после выбора поставщика OLE DB** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


Открывается вкладка **Подключение**. 

1. Выберите файл базы данных Microsoft Access (в нашем случае db.mdb) и щелкните **ОК**.
   **Щелкните кнопку ОК после выбора файла базы данных** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

После нажатия **ОК** будет создано подключение к базе данных Microsoft Access в **Обозревателе сервера**. Дважды щелкните на подключении, чтобы увидеть все таблицы, представления и хранимые процедуры в базе данных.

{{% /alert %}} 
### **Шаг 4: Создание объектов подключения к базе данных графически**
1. Просмотрите таблицы в базе данных с помощью **Обозревателя сервера**.
   Есть только одна таблица, Продукты. 
1. Перетащите таблицу Продукты из **Обозревателя сервера** на **Веб-форму**.
   **Перетаскивание таблицы Продукты из Обозревателя сервера и отпускание на веб-форму** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



Может появиться диалоговое окно.
**Диалог для подтверждения включения пароля от базы данных в строке подключения** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



Решите, хотите ли вы включить пароль от базы данных в строку подключения или нет. В этом примере мы выбрали **Не включать пароль**. 
Были созданы и добавлены два объекта подключения к базе данных (oleDbConnection1 и oleDbDataAdapter1).
**Создано и отображено объекты подключения к базе данных (oleDbConnection1 & oleDbDataAdapter1)** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Шаг 5: Генерация набора данных**
До сих пор мы создали объекты подключения к базе данных, но все еще нужно где-то хранить данные после подключения к базе данных. Объект DataSet может хранить данные точно, и их также легко генерировать с помощью среды VS.NET. 

1. Выберите **oleDbDataAdaper1** и щелкните правой кнопкой мыши.
1. Выберите **Сгенерировать набор данных** из меню.
   **Выбор опции Генерировать набор данных** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



Отображается диалоговое окно Генерировать набор данных. 
Здесь можно выбрать имя для нового объекта DataSet, который должен быть создан, и какие таблицы следует добавить к нему. 

1. Выберите опцию **Добавить этот набор данных в дизайнер**.
1. Нажмите **ОК**.
   **Щелкните кнопку ОК для создания DataSet** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



Объект dataSet11 добавлен в дизайнер.
**Набор данных создан и добавлен в дизайнер** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Шаг 6: Использование конструктора рабочих листов**
Теперь пришло время открыть секрет. 

1. Выберите элемент управления GridWeb и нажмите правой кнопкой мыши.
1. Выберите опцию **Конструктор рабочих листов** из меню. 

   **Выбор опции Конструктор рабочих листов** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



Отображается редактор коллекции рабочих листов (также называемый конструктором рабочих листов). 
**Диалоговое окно Редактора коллекции рабочих листов** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



Диалоговое окно содержит несколько свойств, которые можно настроить для привязки Лист1 к любой таблице в базе данных.

1. Выберите свойство **ИсточникДанных**.
   Объект dataSet11, созданный на предыдущем этапе, отображается в меню. 
1. Выберите dataSet11.
1. Нажмите свойство **DataMember**.
   Пользовательский конструктор рабочих листов автоматически показывает список таблиц в dataSet11. Там есть только одна таблица, Products.
1. Выберите таблицу Products.
   **Настройка свойств DataSource и DataMember** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. Проверьте свойство **BindColumns**.
   **Нажатие на свойство BindColumns** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



Нажатие на свойство **BindColumns** открывает редактор коллекции BindColumn.
**Редактор коллекции BindColumn** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



В редакторе коллекции BindColumn все столбцы таблицы **Products** автоматически добавляются в коллекцию BindColumns. 

1. Выберите любой столбец и настройте его свойства.
   Например, вы можете изменить подпись каждого столбца.
   **Изменение подписи столбца ProductID** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. После внесения изменений нажмите **OK**.
1. Закройте все диалоговые окна, нажав **OK**.
   Наконец, вы вернетесь на страницу WebForm1.aspx. 
   **Возвращение на страницу WebForm1.aspx после использования конструктора рабочих листов** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


Выше показаны названия столбцов таблицы Products. Ширина столбцов мала, поэтому полные названия некоторых столбцов не полностью видны. 
### **Шаг 7: Добавление кода в обработчик события Page_Load**
Мы использовали конструктор рабочих листов и теперь просто должны добавить код в обработчик события Page_Load для заполнения объекта dataSet11 данными из базы данных (с использованием oleDbDataAdapter1) и привязки элемента управления GridWeb к dataSet11, вызвав его метод DataBind. 

1. Добавьте код: 

**C#**

{{< highlight csharp >}}

 //Implementing Page_Load event handler

private void Page_Load(object sender, System.EventArgs e)

{

    //Checking if there is not any PostBack

    if (!IsPostBack)

    {

        try

        {

            //Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11);

            //Binding GridWeb with DataSet

            GridWeb1.DataBind();

        }

        finally

        {

            //Finally, closing database connection

            oleDbConnection1.Close();

        }

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Implementing Page_Load event handler

Private Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Checking if there is not any PostBack

    If Not IsPostBack Then

        Try

            'Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11)

            'Binding GridWeb with DataSet

            GridWeb1.DataBind()

        Finally

            'Finally, closing database connection

            oleDbConnection1.Close()

        End Try

    End If

End Sub



{{< /highlight >}}

1. Проверьте код, добавленный в обработчик события Page_Load.
   **Код добавлен в обработчик события Page_Load** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Шаг 8: Запуск приложения**
Скомпилируйте и запустите приложение: нажмите **Ctrl+F5** или щелкните **Start**. 
**Запуск приложения** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



После компиляции страница WebForm1.aspx открывается в окне браузера со всеми данными, загруженными из базы данных.
**Данные загружены в элемент управления GridWeb из базы данных** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **Работа с элементом управления GridWeb**
Когда данные загружаются в элемент управления GridWeb, пользователи получают возможность управлять данными. GridWeb предлагает ряд различных функций манипуляции данными. 
### **Валидация данных**
Aspose.Cells.GridWeb автоматически создает соответствующие правила валидации для всех привязанных столбцов в соответствии с типами данных, определенными в базе данных. Узнайте тип валидации ячейки, наведя указатель мыши на нее.
**Проверка типа валидации ячейки** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

Here, the selected cell contains the **<INT>** validation, which means that users can only enter integer values into it. If they enter another value, a validation error occurs. Moreover, **<REQUIRED>** shows that the value Product ID must be submitted. 
### **Удаление строк**
Чтобы удалить строку, выберите строку (или любую ячейку в строке), щелкните правой кнопкой мыши и выберите **Удалить строку**.
**Выбор опции Удалить строку из меню** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


Строка будет немедленно удалена.
**Данные элемента управления после удаления строки** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Редактирование строк**
Отредактируйте данные в ячейках или строках, а затем нажмите **Сохранить** или **Отправить** для сохранения изменений. 
### **Добавление строк**
1. Чтобы добавить строку, щелкните правой кнопкой мыши по ячейке и выберите **Добавить строку**.
   **Выбор опции Добавить строку из меню** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



Новая строка добавляется в лист в конец других строк.
**Добавлена новая строка в таблицу** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



At the left of the new row is an asterisk {{< emoticons/cross >}}, indicating that the row is new. 

1. Добавьте значения в новую строку.
1. Нажмите **Сохранить** или **Отправить**, чтобы подтвердить изменение.
   **Сохранение изменений в данных, нажав кнопку *Сохранить*** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Настройка числового формата**
В данный момент цены в столбце **Цена продукта** отображаются как числовые значения. Их можно преобразовать в вид валюты.

1. Вернитесь в Visual Studio.NET.
1. Откройте редактор сборки BindColumn.
   Свойство **NumberType** столбца **Цена продукта** установлено на **Общий**.
   **Свойство NumberType установлено на Общий** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. Нажмите **DropDownList** и выберите **Currency4** из списка.
   **Свойство NumberType изменено на Валюта4** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Запустите приложение снова.
   Значения в столбце **Цена продукта** теперь отображаются как валюта.
   **Цены продуктов в формате числа валюты** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Редактирование данных**
До сих пор приложение позволяет своим пользователям только просматривать данные таблицы. Пользователи могут редактировать данные в элементе управления GridWeb, но при закрытии браузера и открытии базы данных ничего не изменится. Внесенные изменения не сохраняются в базе данных. 

В следующем примере добавляется код в приложение, чтобы GridWeb мог сохранять изменения в базе данных. 

1. Откройте панель **Свойства** и выберите событие SaveCommand элемента управления GridWeb из списка.
   **Выбор события SaveCommand GridWeb** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. Дважды щелкните событие **SaveCommand**, и VS.NET создаст обработчик события GridWeb1_SaveCommand.
1. Добавьте код в этот обработчик событий, который будет обновлять базу данных с любыми измененными данными в DataSet, привязанном к рабочему листу с использованием oleDbDataAdapter1. 

**C#**

{{< highlight csharp >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WorkSheets[0].DataSource;

        //Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset);

    }

    finally

    {

        //Closing database connection

        oleDbConnection1.Close();

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WorkSheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}

Вы также можете проверить код, добавленный в обработчик события GridWeb1_SaveCommand
**Код, добавленный в обработчик события GridWeb1_SaveCommand** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

Сохранение изменений в базе данных с помощью кнопки **Сохранить** теперь точно сохраняет их.
## **Заключение**
{{% alert color="primary" %}} 

Привязка данных является важной функцией Aspose.Cells.GridWeb. Легко привязывать рабочие листы к базе данных с помощью утилиты Worksheets Designer, предлагаемой Aspose.Cells.GridWeb. Aspose.Cells.GridWeb экономит время и усилия при создании мощных решений на основе сетки. 

{{% /alert %}}
