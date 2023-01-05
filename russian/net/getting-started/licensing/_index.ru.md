---
title: Лицензирование
type: docs
weight: 120
url: /ru/net/licensing/
---
{{% alert color="primary" %}}

 Вы можете легко загрузить ознакомительную версию Aspose.Cells со своего[страница загрузки](https://www.nuget.org/packages/Aspose.Cells) @ NuGet репозиторий. Ознакомительная версия предоставляет абсолютно те же возможности, что и лицензионная версия компонента. Кроме того, ознакомительная версия просто становится лицензируемой, когда вы покупаете лицензию и добавляете пару строк кода для применения лицензии.

{{% /alert %}}

## **Ограничения ознакомительной версии**

Оценочная версия продукта Aspose.Cells (без указания лицензии) обеспечивает полную функциональность продукта, но она ограничена открытием 100 файлов в одной программе и дополнительным рабочим листом с водяным знаком оценки.

Ограничения показаны ниже:

- **Количество открытых файлов** (Aspose.Cells)
При запуске вашей программы вы можете открыть только 100 файлов Excel, используя библиотеку Aspose.Cells. Если ваше приложение превысит это число, будет выдано исключение.
- **Настройки файла конфигурации** (Aspose.Cells.GridWeb)
 Вы не можете повторно указать путь к сценарию, добавив следующие строки кода в раздел конфигурации (например, в файл web.config). acw_client — это папка, содержащая файлы, и Aspose.Cells. GridWeb использует эту папку для управления своей внутренней конфигурацией, в ней есть файлы сценариев, файлы изображений и другие файлы для определения поведения GridWeb и настройки других операций. Файл конфигурации используется для предотвращения использования элементом управления встроенных клиентских ресурсов (изображений, сценариев и т. д.), что полезно в некоторых случаях/сценариях. Кроме того, эти параметры конфигурации в файле web.config вступят в силу только с ЛИЦЕНЗИОННОЙ версией элемента управления.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Эти настройки могут быть обязательными в некоторых случаях / сценариях, если вы используете элемент управления Aspose.Cells.GridWeb на веб-сайтах файловой системы или в расширениях MS Ajax и т. д.

{{% /alert %}}

Кроме того, рабочий лист с водяным знаком оценки всегда будет отображаться как активный рабочий лист в сгенерированном файле Excel с использованием библиотеки Aspose.Cells. Только в лицензионной версии вы можете установить активный рабочий лист на другие рабочие листы. В выходном файле PDF или файле изображения Aspose.Cells водяной знак оценки будет вставлен в верхнюю часть документа/изображения. Вы также не можете скрыть предупреждение об авторских правах оценки (дополнительный рабочий лист) в элементе управления GridWeb, он всегда будет добавлен (в конце вкладок рабочего листа) в элементе управления.

{{% alert color="primary" %}}

 Если вы хотите протестировать Aspose.Cells без ограничений ознакомительной версии, вы также можете запросить[30-дневная временная лицензия](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Применение лицензии в компоненте Aspose.Cells**

Лицензия представляет собой простой текстовый XML-файл, который содержит такие сведения, как название продукта, количество разработчиков, для которых он лицензируется, дату истечения срока действия подписки и т. д. Файл имеет цифровую подпись, поэтому не изменяйте файл. Даже непреднамеренное добавление дополнительного разрыва строки в файл сделает его недействительным. Вам необходимо установить лицензию перед использованием Aspose.Cells, если вы хотите избежать ограничения его оценки. Для каждого приложения (или процесса) требуется установить лицензию только один раз. Лицензия может быть загружена из файла, потока или встроенного ресурса.

Aspose.Cells пытается найти лицензию в следующих местах:

- Явный путь
- Папка, содержащая Aspose.Cells.dll
- Папка, содержащая сборку с именем Aspose.Cells.dll
- Папка, содержащая сборку записи (ваш .exe)
- Встроенный ресурс в сборке, вызывающий Aspose.Cells.dll.

Существует два распространенных метода применения лицензии: из файла или потока или в виде встроенного ресурса.

### **Применение лицензии с диска или потока**

Самый простой способ установить лицензию — положить файл лицензии в ту же папку, что и Aspose.Cells.dll, и указать только имя файла без пути к нему.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

 При вызове метода SetLicense имя лицензии должно совпадать с именем вашего файла лицензии. Например, вы можете изменить имя файла лицензии на**Aspose.Cells.lic.xml**. Затем в вашем коде вы должны использовать измененное имя лицензии (**Aspose.Cells.lic.xml**) для метода SetLicense.

{{% /alert %}}

Также можно загрузить лицензию из потока.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Применение ограниченной лицензии**

Aspose.Cells позволяет разработчикам применять лимитный ключ. Это новый механизм лицензирования. Новый механизм лицензирования будет использоваться наряду с существующим методом лицензирования. Те клиенты, которые хотят получать счета на основе использования функций API, могут использовать лимитное лицензирование. Для получения более подробной информации см.[Часто задаваемые вопросы об ограниченном лицензировании](https://purchase.aspose.com/faqs/licensing/metered)раздел.

Новый класс[Измеренный](https://reference.aspose.com/cells/net/aspose.cells/metered)был введен для применения измеренного ключа. Ниже приведен пример кода, демонстрирующий, как установить открытый и закрытый ключ с измерителем.

{{< highlight "csharp" >}}

 //Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.SetMeteredKey("*************", "*************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

Console.WriteLine(workbook.IsLicensed);

//Get the Consumption quantity

decimal amountBefore = Metered.GetConsumptionQuantity();

Console.WriteLine(amountBefore);

Workbook workbook2 = new Workbook("e:\\test2\\Book1.xlsx");

workbook2.Save("e:\\test2\\out1.xlsx");

//Since uploading data is already running on another thread, so you might need to wait for some time (optional)

System.Threading.Thread.Sleep(10000);

//Get the Consumption quantity again which should be greater a bit

decimal amountAfter = Metered.GetConsumptionQuantity();

Console.WriteLine(amountAfter);

{{< /highlight >}}

### **Использование встроенного ресурса**

Еще один удобный способ упаковать лицензию вместе с приложением и убедиться, что она не будет утеряна, — включить ее в качестве встроенного ресурса в одну из сборок, вызывающих Aspose.Cells. Чтобы включить файл лицензии в качестве встроенного ресурса, выполните следующие действия. :

1.  В Visual Studio .NET включите файл лицензии (.lic) в проект, выбрав**Добавить существующий элемент** от**Файл** меню.
1. Выберите файл в обозревателе решений и установите**Построить действие** к**Встроенный ресурс** в окне свойств

 Для доступа к встроенной в сборку лицензии (как внедренному ресурсу) не требуется вызывать методы GetExecutingAssembly и GetManifestResourceStream класса System.Reflection.Assembly Microsoft .NET Framework. Все, что нужно сделать, это просто добавить файл лицензии в качестве встроенного ресурса в ваш проект и передать имя файла лицензии в метод SetLicense.**Aspose.Cells.License** class автоматически найдет файл лицензии во встроенных ресурсах. Пожалуйста, просмотрите приведенный ниже пример, чтобы понять этот метод установки лицензии (встроенной) в ваших приложениях.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Установка лицензии в Aspose.Cells Grid Controls**

В Aspose.Cells Grid Suite лицензия может быть загружена из файла, потока или встроенного ресурса. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb пытается найти лицензию в следующих местах:

1. Явный путь
1. Папка, содержащая DLL компонента (входит в состав Aspose.Cells.GridDesktop или Aspose.Cells.GridWeb).
1. Папка, содержащая сборку, вызывающую DLL компонента (входит в состав Aspose.Cells.GridDesktop или Aspose.Cells.GridWeb).
1. Папка, содержащая сборку записи (ваш .exe)
1. Встроенный ресурс в сборке, вызывающий DLL компонента (входит в состав Aspose.Cells.GridDesktop или Aspose.Cells.GridWeb).

{{% alert color="primary" %}}

Если вы используете элемент управления Aspose.Cells.GridDesktop, класс лицензии будет использоваться как Aspose.Cells.GridDesktop.License, но если вы используете элемент управления Aspose.Cells.GridWeb, то для установки лицензии будет использоваться класс Aspose.Cells.GridWeb.License.

{{% /alert %}}

### **Применение лицензии с диска или потока**

Самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и dll компонента (входит в состав Aspose.Cells.GridWeb), и указать только имя файла без пути к нему.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Когда вы вызываете метод SetLicense, имя лицензии должно совпадать с именем вашего файла лицензии. Например, вы можете изменить имя файла лицензии на «MyLicense.lic.xml». Затем в своем коде вы должны использовать измененное имя лицензии (то есть MyLicense.lic.xml) для метода SetLicense.

{{% /alert %}}

Также можно загрузить лицензию из потока.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Применение лицензии в качестве встроенного ресурса**

Еще один удобный способ упаковать лицензию вместе с вашим приложением и убедиться, что она не будет потеряна, — включить ее в качестве встроенного ресурса в одну из сборок, которая вызывает dll компонента (входит в состав Aspose.Cells.GridDesktop). Чтобы включить файл лицензии в качестве встроенного ресурса, выполните следующие действия:

1.  В Visual Studio .NET включите файл лицензии (.lic) в проект с помощью**Добавить существующий элемент** вариант на**Файл** меню.
1. Выберите файл в обозревателе решений и установите для параметра «Действие сборки» значение «Встроенный ресурс» в окне «Свойства».
1. Для доступа к лицензии, встроенной в сборку (как встроенный ресурс), не требуется вызывать методы GetExecutingAssembly и GetManifestResourceStream класса System.Reflection.Assembly Microsoft .NET Framework. Вместо этого добавьте файл лицензии в качестве встроенного ресурса в свой project и передайте имя файла лицензии в метод SetLicense. Класс License автоматически находит файл лицензии во встроенных ресурсах.

Пожалуйста, просмотрите приведенный ниже пример, чтобы понять этот метод применения лицензии в качестве встроенного ресурса к вашим приложениям.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **Применение лицензии в Aspose.Cells.GridDesktop для приложения WinForm**

Рекомендуется вводить лицензионный код перед запуском приложения и применять его только один раз. Например, для приложения Windows C# поместите лицензионный код в метод Main.

{{< highlight "csharp" >}}

public class Form1 : System.Windows.Forms.Form

{

private Aspose.Cells.GridDesktop.GridDesktop gridDesktop1;

/// <summary>

/// Required designer variable.

/// </summary>

private System.ComponentModel.Container components = null;

public Form1()

{

//

// Required for Windows Form Designer support

//

InitializeComponent();

//

// TODO: Add any constructor code after InitializeComponent call

//

}

/// The main entry point for the application.

/// </summary>

.

.

.

.

[STAThread]

static void Main()

{

Aspose.Cells.GridDesktop.License lic = new Aspose.Cells.GridDesktop.License();

//Use this line if you are using an explicit path for the license file.

lic.SetLicense(@"C:\MyLicense.lic");

//Or use the line below if you are using the license file as an embedded resource.

//lic.SetLicense("MyLicense.lic");

Application.Run(new Form1());

}

private void Form1_Load(object sender, System.EventArgs e)

{

Aspose.Cells.GridDesktop.Worksheet sheet = this.gridDesktop1.Worksheets.Add("MySheet");

sheet.Cells["A1"].SetCellValue("Hello");

gridDesktop1.ActiveSheetIndex = 1;

}

}

{{< /highlight >}}

## **Примечания по применению лицензии в Aspose.Cells.GridWeb**

Рекомендуется поместить лицензионный код в Global.asax.cs вашего веб-приложения (предполагается, что этот лицензионный файл находится на диске " d:\ "):

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Загрузка лицензии из потока

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
