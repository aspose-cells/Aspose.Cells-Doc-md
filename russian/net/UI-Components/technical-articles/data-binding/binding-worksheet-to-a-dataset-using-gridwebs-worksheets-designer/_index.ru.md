---
title: Привязка рабочего листа к набору данных с помощью конструктора рабочих листов GridWebs
type: docs
weight: 20
url: /ru/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/
---
{{% alert color="primary" %}} 

 В этой статье обсуждается простой подход к привязке рабочих листов к таблицам базы данных в режиме графического интерфейса пользователя с помощью специального инструмента, входящего в состав Aspose.Cells.GridWeb, дизайнера рабочих листов.

{{% /alert %}} 
## **Связывание рабочего листа с базой данных с помощью Worksheets Designer**
	**Шаг 1: Создание образца базы данных**
1. Сначала мы создадим образец базы данных, который будет использоваться в этой статье. Мы используем Microsoft Access для создания базы данных, содержащей таблицу с названием Products. Его схема показана ниже.
   **Информация о дизайне таблицы «Продукты»** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. В таблицу «Продукты» добавлено несколько фиктивных записей.
   **Записи в таблице «Товары»** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Шаг 2: Разработка примера приложения**
 Веб-приложение ASP.NET создается и разрабатывается в Visual Studio.NET, как показано ниже.
**Образец разработанного приложения** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Шаг 3. Подключение к базе данных с помощью обозревателя серверов**
 Пришло время подключиться к базе данных. Мы можем сделать это легко, используя Server Explorer в Visual Studio.NET.

1.  Выбирать**Подключение для передачи данных** в**Обозреватель серверов** и щелкните правой кнопкой мыши.
1.  Выбирать**Добавить соединение** из меню.
   **Выбор опции «Добавить соединение»** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



 Отображается диалоговое окно Свойства канала передачи данных.
**Диалоговое окно «Свойства канала передачи данных»** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



 С помощью этого диалога вы можете подключиться к любой базе данных. По умолчанию он позволяет подключаться к базе данных SQL Server. В этом примере нам нужно подключиться к базе данных Access Microsoft.

1.  Нажмите на**Провайдер** вкладка
1.  Выбирать**Microsoft Поставщик Jet 4.0 OLE DB** от**Поставщик(и) OLE DB** список.
1.  Нажмите**Следующий**.
   **Нажмите «Далее» после выбора поставщика OLE DB.** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


**Связь** вкладка открыта.

1.  Выберите файл базы данных Access Microsoft (в нашем случае db.mdb) и нажмите**ХОРОШО**.
   **Нажатие кнопки OK после выбора файла базы данных** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

 После нажатия**ХОРОШО** , соединение с базой данных Microsoft Access будет создано в**Обозреватель серверов**Дважды щелкните соединение, чтобы увидеть все таблицы, представления и хранимые процедуры в базе данных.

{{% /alert %}} 
### **Шаг 4. Графическое создание объектов подключения к базе данных**
1.  Просмотрите таблицы в базе данных с помощью**Обозреватель серверов**.
 Есть только одна таблица, Продукты.
1.  Перетащите таблицу «Продукты» из**Обозреватель серверов** к**Веб-форма**.
   **Перетаскивание таблицы «Продукты» из обозревателя серверов в веб-форму** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



Может появиться диалоговое окно.
**Диалоговое окно для подтверждения включения пароля базы данных в строку подключения** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



 Решите, хотите ли вы включить пароль базы данных в строку подключения или нет. Для этого примера мы выбрали**Не включать пароль**. 
Созданы и добавлены два объекта подключения к базе данных (oleDbConnection1 и oleDbDataAdapter1).
**Объекты подключения к базе данных (oleDbConnection1 и oleDbDataAdapter1), созданные и отображаемые** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Шаг 5: Создание набора данных**
До сих пор мы создали объекты подключения к базе данных, но нам все еще нужно где-то хранить данные после подключения к базе данных. Объект DataSet может точно хранить данные, и мы также можем легко сгенерировать его с помощью VS.NET IDE.

1.  Выбирать**оледбдатаадапер1** и щелкните правой кнопкой мыши.
1.  Выбирать**Создать набор данных** вариант из меню.
   **Выбор параметра «Создать набор данных»** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



 Отображается диалоговое окно «Создать набор данных».
 Здесь можно выбрать имя для создаваемого нового объекта DataSet и таблицы, которые следует к нему добавить.

1.  Выберите**Добавьте этот набор данных в дизайнер** вариант.
1.  Нажмите**ХОРОШО**.
   **Нажатие кнопки OK для создания DataSet** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



В дизайнер добавлен объект dataSet11.
**Набор данных создан и добавлен в конструктор** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Шаг 6: Использование конструктора рабочих листов**
 Теперь пришло время открыть секрет.

1. Выберите элемент управления GridWeb и щелкните правой кнопкой мыши.
1.  Выбирать**Дизайнер рабочих листов** вариант из меню.

   **Выбор опции «Конструктор рабочих листов»** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



 Отображается редактор коллекции рабочих листов (также называемый дизайнером рабочих листов).
**Диалоговое окно «Редактор коллекции рабочих листов»** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



Диалоговое окно содержит несколько свойств, которые можно настроить для привязки Sheet1 к любой таблице в базе данных.

1.  Выберите**Источник данных** имущество.
 Объект dataSet11, сгенерированный на предыдущем шаге, указан в меню.
1. Выберите набор данных11.
1.  Нажмите на**DataMember** имущество.
 Конструктор рабочих листов автоматически показывает список таблиц в dataSet11. Есть только одна таблица, Продукты.
1. Выберите таблицу «Продукты».
   **Установка свойств DataSource и DataMember** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1.  Проверить**БиндКолонкс** имущество.
   **Щелчок по свойству BindColumns** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



 Нажав на**БиндКолонкс** Свойство открывает редактор коллекции BindColumn.
**Редактор коллекций BindColumn** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



 В редакторе коллекции BindColumn все столбцы**Товары** table автоматически добавляются в коллекцию BindColumns.

1. Выберите любой столбец и настройте его свойства.
 Например, вы можете изменить заголовок каждого столбца.
   **Изменение заголовка столбца ProductID** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1.  После внесения изменений нажмите**ХОРОШО**.
1.  Закройте все диалоги, нажав**ХОРОШО**.
 Наконец, вы вернетесь на страницу WebForm1.aspx.
   **Возврат на страницу WebForm1.aspx после использования конструктора рабочих листов** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


 Выше показано имя столбца таблицы «Продукты». Ширина столбцов мала, поэтому полные названия некоторых столбцов видны не полностью.
### **Шаг 7: Добавление кода в обработчик событий Page_Load**
 Мы воспользовались конструктором рабочих листов и теперь просто должны добавить код в обработчик событий Page_Load для заполнения объекта dataSet11 данными из базы данных (используя oleDbDataAdapter1) и привязки элемента управления GridWeb к dataSet11 путем вызова его метода DataBind.

1.  Добавьте код:

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

1. Проверьте код, добавленный в обработчик событий Page_Load.
   **Код добавлен в обработчик событий Page_Load** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Шаг 8: Запуск приложения**
 Скомпилируйте и запустите приложение: либо нажмите**Ctrl+F5** или нажмите**Начинать**. 
**Запуск приложения** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



После компиляции в окне браузера открывается страница WebForm1.aspx со всеми данными, загруженными из базы данных.
**Данные, загруженные в элемент управления GridWeb из базы данных** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **Работа с элементом управления GridWeb**
 Когда данные загружаются в элемент управления GridWeb, он предоставляет пользователям контроль над данными. GridWeb предлагает ряд различных типов функций манипулирования данными.
### **Проверка данных**
Aspose.Cells.GridWeb автоматически создает соответствующие правила проверки для всех связанных столбцов в соответствии с типами данных, определенными в базе данных. Просмотрите тип проверки ячейки, наведя на нее курсор.
**Проверка типа проверки ячейки** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

 Здесь выбранная ячейка содержит**<INT>** валидация, что означает, что пользователи могут вводить в него только целочисленные значения. Если они вводят другое значение, возникает ошибка проверки. Более того,**<ОБЯЗАТЕЛЬНО>** показывает, что значение Product ID должно быть представлено.
### **Удаление строк**
 Чтобы удалить строку, выберите строку (или любую ячейку в строке), щелкните правой кнопкой мыши и выберите**Удалить строку**.
**Выбор опции Удалить строку из меню** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


Строка будет удалена мгновенно.
**Данные сетки (после удаления строки)** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Редактирование строк**
Отредактируйте данные в ячейках или строках, а затем щелкните**Сохранять** или же**Представлять на рассмотрение** чтобы сохранить изменения.
### **Добавление строк**
1.  Чтобы добавить строку, щелкните ячейку правой кнопкой мыши и выберите**Добавить ряд**.
   **Выбор опции «Добавить строку» в меню** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



Новая строка добавляется на лист в конце других строк.
**В сетку добавлена новая строка** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



 Слева от новой строки стоит звездочка{{< emoticons/cross >}} , указывая на то, что строка новая.

1. Добавьте значения в новую строку.
1.  Нажмите**Сохранять** или же**Представлять на рассмотрение** чтобы подтвердить изменение.
   **Сохранение изменений в данных нажатием кнопки *Сохранить** кнопка*

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Настройка числового формата**
 На данный момент цены в**Цена продукта** столбец отображаются в виде числовых значений. Можно сделать их похожими на валюту.

1. Вернитесь в Visual Studio.NET.
1. Откройте редактор коллекции BindColumn.
**Тип номера** собственность**Цена продукта** столбец настроен на**Общий**.
   **Для свойства NumberType задано значение General.** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1.  Нажмите**Выпадающий список** и выберите**Валюта4** из списка.
   **Свойство NumberType изменено на Currency4.** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Запустите приложение еще раз.
 Значения в**Цена продукта** столбец теперь является валютой.
   **Цены на товары в валюте Числовой формат** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Редактирование данных**
 Приложение пока позволяет своим пользователям только просматривать табличные данные. Пользователи могут редактировать данные в элементе управления GridWeb, но при закрытии браузера и открытии базы данных ничего не меняется. Внесенные изменения не сохраняются в базе данных.

 В следующем примере в приложение добавляется код, чтобы GridWeb мог сохранять изменения в базе данных.

1. Открой**Характеристики** и выберите из списка событие SaveCommand элемента управления GridWeb.
   **Выбор события SaveCommand GridWeb** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1.  Дважды щелкните**СохранитьКоманда** событие, а VS.NET создает обработчик событий GridWeb1_SaveCommand.
1.  Добавьте в этот обработчик событий код, который будет обновлять базу данных любыми измененными данными в наборе данных, привязанном к рабочему листу с помощью oleDbDataAdapter1.

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WebWorksheets[0].DataSource;

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

{{< highlight "csharp" >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WebWorksheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}

Вы также можете проверить код, добавленный в обработчик событий GridWeb1_SaveCommand.
**Код, добавленный в обработчик событий GridWeb1_SaveCommand** 

![дело:изображение_альтернативный_текст](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

 Сохраните изменения в базе данных с помощью**Сохранять** кнопка теперь определенно сохраняет их.
## **Вывод**
{{% alert color="primary" %}} 

Привязка данных — важная функция Aspose.Cells.GridWeb. Рабочие листы легко привязать к базе данных с помощью утилиты Worksheets Designer, предлагаемой Aspose.Cells.GridWeb. Aspose.Cells.GridWeb экономит время и усилия при создании мощных грид-решений.

{{% /alert %}}
