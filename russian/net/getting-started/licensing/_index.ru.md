---
title: Лицензирование
type: docs
weight: 120
url: /ru/net/licensing/
description: Aspose.Cells for .NET предоставляет различные планы для покупки или предлагает бесплатную пробную версию и временную лицензию на 30 дней для оценки с использованием политик лицензирования и подписки на C#.
keywords: C# Применение лицензии с диска или потока. C# Установить лицензию с диска или потока. Применить лицензию в Aspose.Cells for NET.
---

## **Как применить лицензию в компонент Aspose.Cells**

Лицензия - это текстовый файл XML, содержащий сведения, такие как название продукта, количество лицензированных разработчиков, дата истечения срока действия подписки и т. д. Файл имеет цифровую подпись, поэтому не изменяйте его. Даже ненамеренное добавление дополнительного символа перехода на новую строку в файл инвалидирует его. Вам нужно установить лицензию перед использованием Aspose.Cells, если вы хотите избежать ограничений на его оценку. Для избежания ограничений лицензию нужно установить только один раз для каждого приложения (или процесса). Лицензию можно загрузить из файла, потока или встроенного ресурса.

Aspose.Cells пытается найти лицензию в следующих местах:

- Явный путь
- Папка, содержащая Aspose.Cells.dll
- Папка, содержащая сборку, вызвавшую Aspose.Cells.dll
- Папка, содержащая входную сборку (ваш .exe)
- Встроенный ресурс в вызывающей Aspose.Cells.dll сборке

Существует два общих метода применения лицензии, из файла или потока, или как встроенный ресурс.

### **Как применить лицензию с диска или потока**

Самый простой способ установить лицензию - поместить файл лицензии в ту же папку, что и Aspose.Cells.dll, и указать только имя файла без его пути.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Когда вы вызываете метод SetLicense, имя лицензии должно совпадать с именем вашего файла лицензии. Например, вы можете изменить имя файла лицензии на **Aspose.Cells.lic.xml**. Затем в своем коде вы должны использовать модифицированное имя лицензии (**Aspose.Cells.lic.xml**) для метода SetLicense.

{{% /alert %}}

Также возможно загрузить лицензию из потока.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Как применить метрическую лицензию**

Aspose.Cells позволяет разработчикам применять метрический ключ. Это новый механизм лицензирования. Новый механизм лицензирования будет использоваться вместе с существующим методом лицензирования. Те клиенты, которые хотят платить в зависимости от использования функций API, могут использовать метрическое лицензирование. Для получения дополнительной информации обратитесь к разделу [Часто задаваемые вопросы о метрическом лицензировании](https://purchase.aspose.com/faqs/licensing/metered).  

Был представлен новый класс [Metered](https://reference.aspose.com/cells/net/aspose.cells/metered) для применения метрического ключа. Ниже приведен пример кода, демонстрирующий, как установить открытый и закрытый метрический ключ.

{{< highlight csharp >}}

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

### **Как использовать встроенный ресурс**

Другой изящный способ упаковки лицензии с вашим приложением и обеспечения ее сохранения - включить ее в качестве встроенного ресурса в одну из сборок, вызывающих Aspose.Cells. Для включения файла лицензии в виде встроенного ресурса выполните следующие шаги:

1. В Visual Studio .NET добавьте файл лицензии (.lic) в проект, выбрав **Добавить существующий элемент** из меню **Файл**.
1. Выберите файл в Обозревателе решений и установите **Действие сборки** в **Встроенный ресурс** в окне Свойства.

Для доступа к лицензии, вложенной в сборку (в виде встроенного ресурса), не требуется вызывать методы GetExecutingAssembly и GetManifestResourceStream класса System.Reflection.Assembly в Microsoft .NET Framework. Достаточно просто добавить файл лицензии в виде встроенного ресурса в ваш проект и передать имя файла лицензии в метод SetLicense. Класс **Aspose.Cells.License** автоматически найдет файл лицензии в встроенных ресурсах. Пожалуйста, ознакомьтесь с приведенным ниже примером, чтобы понять этот метод установки лицензии (встроенной) в ваши приложения.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Как установить лицензию в элементах управления сеткой Aspose.Cells**

В наборе сетки Aspose.Cells лицензию можно загрузить из файла, потока или встроенного ресурса. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb пытаются найти лицензию в следующих местах:

1. Явный путь
1. Папка, содержащая dll компонента (включенного в Aspose.Cells.GridDesktop или Aspose.Cells.GridWeb)
1. Папка, содержащая сборку, вызвавшую dll компонента (включенного в Aspose.Cells.GridDesktop или Aspose.Cells.GridWeb)
1. Папка, содержащая входную сборку (ваш .exe)
1. Встроенный ресурс в сборке, вызвавшей dll компонента (включенной в Aspose.Cells.GridDesktop или Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

Если вы используете элемент управления Aspose.Cells.GridDesktop, то для установки лицензии будет использоваться класс Aspose.Cells.GridDesktop.License, но если вы используете элемент управления Aspose.Cells.GridWeb, то будет использоваться класс Aspose.Cells.GridWeb.License для установки лицензии.

{{% /alert %}}

### **Как применить лицензию с диска или потока**

Самый простой способ установить лицензию - поместить файл лицензии в ту же папку, что и dll компонента (включенной в Aspose.Cells.GridWeb) и указать только его имя без пути.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Когда вы вызываете метод SetLicense, имя лицензии должно совпадать с именем вашего файла лицензии. Например, вы можете изменить имя файла лицензии на "MyLicense.lic.xml". Затем в своем коде вы должны использовать измененное имя лицензии (т.е. MyLicense.lic.xml) для метода SetLicense.

{{% /alert %}}

Также возможно загрузить лицензию из потока.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Как применить лицензию как встроенный ресурс**

Еще один удобный способ упаковки лицензии с вашим приложением и обеспечения того, что она не будет потеряна, - это включить ее в качестве встроенного ресурса в одну из сборок, вызывающих dll компонента (включенного в Aspose.Cells.GridDesktop). Чтобы включить файл лицензии в качестве встроенного ресурса, выполните следующие шаги:

1. В Visual Studio .NET добавьте файл лицензии (.lic) в проект, используя опцию **Добавить существующий элемент** в меню **Файл**.
1. Выберите файл в Обозревателе решений и установите действие сборки в Embedded Resource в окне Свойств.
1. Для доступа к лицензии, встроенной в сборку (как встроенный ресурс), не нужно вызывать методы GetExecutingAssembly и GetManifestResourceStream класса System.Reflection.Assembly в Microsoft .NET Framework. Вместо этого добавьте файл лицензии в качестве встроенного ресурса в свой проект и передайте имя файла лицензии в метод SetLicense. Класс License автоматически найдет файл лицензии во встроенных ресурсах.

Пожалуйста, ознакомьтесь с приведенным ниже примером, чтобы понять этот метод применения лицензии как встроенного ресурса в ваши приложения.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **Как применить лицензию в Aspose.Cells.GridDesktop для приложения WinForm**

Рекомендуется разместить свой код лицензирования перед запуском вашего приложения и применить его только один раз. Например, для приложения C# Windows разместите код лицензирования в методе Main.

{{< highlight csharp >}}

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

Рекомендуется разместить код лицензирования в Global.asax.cs вашего веб-приложения (предполагается, что этот файл лицензии размещен на диске "d:\").

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Загрузка лицензии из потока

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
