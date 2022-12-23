---
title: Çalışma Sayfasını GridWeb Kullanarak Özelleştirilmiş Bir Koleksiyon Nesnesine Bağlama
type: docs
weight: 130
url: /tr/net/binding-worksheet-to-a-customized-collection-object-using-gridweb/
---
{{% alert color="primary" %}} 

 Microsoft .NET Çerçevesi birçok koleksiyon sınıfı sunar, ancak bazen geliştiricilerin oluşturması için geliştirme gereksinimlerini karşılamazlar.**özel koleksiyonlar**ve bu tür özel koleksiyonları Aspose.Cells.GridWeb ile bağlamayı gerektirebilir.

{{% /alert %}} 
## **Çalışma Sayfasını Özel Koleksiyonla Bağlama**
Bu özelliği göstermek için, bu makale örnek bir uygulamanın nasıl oluşturulacağını adım adım açıklamaktadır. Önce özel bir koleksiyon oluşturun ve ardından bu koleksiyonu bir çalışma sayfasıyla ciltlemek için kullanın.
### **1. Adım: Özel Kayıt Oluşturma**
Özel bir koleksiyon oluşturmadan önce, koleksiyonda depolanacak özel kayıtları tutmak için bir sınıf oluşturun. Bu makalenin amacı, kendi özel koleksiyonlarınızı nasıl oluşturacağınız ve bunları Aspose.Cells.GridWeb ile nasıl bağlayacağınız konusunda bir fikir vermektir, böylece özel kaydı nasıl oluşturacağınız size kalmıştır.

Aşağıdaki örnek, özel alanlara erişimi kontrol eden beş özel alan ve beş genel özellik içeren MyCustomRecord sınıfını kullanır. İşte özelliklerin yapısı:

-  Okumak ve yazmak için StringField1 özelliği**stringfield1** (sicim).
-  Yalnızca okunacak ReadonlyField2 özelliği**stringfield2** (sicim).
-  Okumak ve yazmak için DateField1 özelliği**tarih alanı1** (TarihSaat).
-  Okumak ve yazmak için IntField1 özelliği**intfield1** (tamsayı).
-  Okumak ve yazmak için DoubleField1 özelliği**çift alan1** (çift).

**C#**

{{< highlight "csharp" >}}

 //Creating a class that will act as record for the custom collection

public class MyCustomRecord

{

    //Private data members

    private string stringfield1;

    private string stringfield2 = "ABC";

    private DateTime datefield1;

    private int intfield1;

    private double doublefield1;

    //Creating a string property

    public string StringField1

    {

        get { return stringfield1; }

        set { stringfield1 = value; }

    }

    //Creating a readonly string property

    public string ReadonlyField2

    {

        get { return stringfield2; }

    }

    //Creating a DateTime property

    public DateTime DateField1

    {

        get { return datefield1; }

        set { datefield1 = value; }

    }

    //Creating an int property

    public int IntField1

    {

        get { return intfield1; }

        set { intfield1 = value; }

    }

    //Creating a double property

    public double DoubleField1

    {

        get { return doublefield1; }

        set { doublefield1 = value; }

    }

}

{{< /highlight >}}
### **2. Adım: Özel Koleksiyon Oluşturma**
Şimdi, müşteri kayıtları eklemek ve bunlara erişmek için özel bir koleksiyon oluşturun. Basitleştirmek için bu örnek, salt okunur bir dizin oluşturucu içeren MyCollection sınıfını kullanır. Bu indeksleyiciyi kullanarak koleksiyonda saklanan herhangi bir özel kaydı alabiliriz.

**C#**

{{< highlight "csharp" >}}

 //Creating a custom collection

public class MyCollection : CollectionBase

{

    //Leaving the collection constructor empty

    public MyCollection()

    {

    }

    //Creating a readonly property for custom collection. This Item property is used by GridWeb control to

    //determine the collection's type

    public MyCustomRecord this[int index]

    {

        get { return (MyCustomRecord)this.List[index]; }

    }

}

{{< /highlight >}}
### **3. Adım: Bir Çalışma Sayfasını Özel Koleksiyonla Bağlama**
Özel koleksiyon oluşturma işlemi tamamlandı. Şimdi Aspose.Cells.GridWeb içindeki bir çalışma sayfasına bağlamak için özel koleksiyonu kullanın. Önce bir web formu oluşturun, buna GridWeb kontrolünü ekleyin ve bazı kodlar ekleyin.

Özel koleksiyonu bağlama amacıyla kullanmak için önce MyCollection sınıfından bir nesne oluşturun (yukarıdaki adımda oluşturuldu).
Ardından MyCustomRecord nesneleri oluşturun ve MyCollection nesnesine ekleyin.

{{% alert color="primary" %}} 

Koleksiyona bir MyCustomRecord nesnesi eklemek için MyCollection sınıfında neden bir yöntem olmadığını merak mı ediyorsunuz? Yukarıdaki koda bir kez daha bakın ve MyCollection sınıfının CollectionBase sınıfından (koleksiyona bir nesne eklemek için bir Add yöntemi sağlayan IList arabirimini uygulayan) miras kaldığını fark edeceksiniz. MyCollection nesnesini IList'e yükselterek IList sınıfının Add yöntemini kullanın.

{{% /alert %}} 

Son olarak, MyCollection nesnesini çalışma sayfasının veri kaynağı olarak ayarlayın ve çalışma sayfasını koleksiyonla bağlayın. Bu noktada, çalışma sayfasının ilişkili sütunları için doğrulama kuralları da oluşturabilirsiniz.

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

{

    if (Page.IsPostBack == false && this.GridWeb1.IsPostBack == false)

    {

        //Creating an object of custom collection

        MyCollection list = new MyCollection();

        //Creating an instance of Random class

        System.Random rand = new System.Random();

        //Creating a loop that will run 5 times

        for (int i = 0; i < 5; i++)

        {

            //Creating an object of Custom Record

            MyCustomRecord rec = new MyCustomRecord();

            //Initializing all properties of Custom Record

            rec.DateField1 = DateTime.Now;

            rec.DoubleField1 = rand.NextDouble() * 10;

            rec.IntField1 = rand.Next(20);

            rec.StringField1 = "ABC_" + i;

            //Adding Custom Record to Collection

            ((IList)list).Add(rec);

        }

        //Accessing a desired worksheet

        GridWorksheet sheet = GridWeb1.WorkSheets[0];

        //Setting the Data Source of worksheet

        sheet.DataSource = list;

        //Creating columns automatically

        sheet.CreateAutoGenratedColumns();

        //Setting the validation type of value to DateTime

        sheet.BindColumns[2].Validation.ValidationType = ValidationType.DateTime;

        //Binding worksheet

        sheet.DataBind();

        //Assigning an event handler to InitializeNewBindRow event of the worksheet

        //sheet.InitializeNewBindRow += new InitializeNewBindRowHandler(GridWeb1_InitializeNewBindRow);

    }

}

{{< /highlight >}}
### **Adım 4: Çalışma Sayfasının InitializeNewBindRow Olayını İşleme**
Yukarıdaki kodda, GridWeb1_InitializeNewBindRow olay işleyicisini çalışma sayfasının InitializeNewBindRow öğesine atamak için kullanılan fazladan bir kod satırı fark etmiş olabilirsiniz. Bu olay, çalışma sayfasına yeni bir ilişkili satır eklendiğinde tetiklenir. MyCustomRecord nesnesinin DateField1 özelliği nedeniyle bu olay için bir olay işleyicisi oluşturduk.

 Aspose.Cells.GridWeb otomatik olarak başlatılır**int** ve**çift** ile değerler**sıfır (0)**GridWeb denetimine yeni bir bağlı satır eklendiğinde. Tarihler için, GridWeb kontrolünün sistemden güncel tarihi otomatik olarak eklemesini istiyoruz. Bunu yapmak için, InitializeNewBindRow olayı için GridWeb1_InitializeNewBindRow olay işleyicisini oluşturduk.

BindObject bağımsız değişkenini kullanarak GridWeb'den MyCustomRecord sınıfının belirli bir örneğine erişin ve ardından geçerli sistem tarihini DateField1 özelliğine atayın.

**C#**

{{< highlight "csharp" >}}

 //Creating GridWeb1_InitializeNewBindRow event handler

private void GridWeb1_InitializeNewBindRow(GridWorksheet sender, object bindObject)

{

    //Accessing that custom record object that is newly bound

    MyCustomRecord rec = (MyCustomRecord)bindObject;

    //Initializing the DateTime of a property when a new row gets bound to the database

    rec.DateField1 = DateTime.Now;

}

{{< /highlight >}}
### **Adım 5: Uygulamayı Çalıştırma**
 ya basarak uygulamayı çalıştırın**Ctrl+F5** veya**Başlama** VS.NET'deki düğme. Web formu yeni bir tarayıcı penceresinde açılır.

**Özel bir koleksiyonla ciltlenmiş çalışma sayfası** 

![yapılacaklar:resim_alternatif_metin](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



 Kayıt eklemek veya silmek için GridWeb denetimine sağ tıklayın. Örneğin, seçerek çalışma sayfasına yeni bir kayıt ekleyin.**Satır ekle** seçenek.

**Menüden Satır Ekle seçeneğinin seçilmesi** 

![yapılacaklar:resim_alternatif_metin](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



 Çalışma sayfasına yeni bir satır eklendiğinde, hücreler geçerli sistem tarihini içeren varsayılan verileri içerir.

**Varsayılan verilerle çalışma sayfasına yeni satır eklendi** 

![yapılacaklar:resim_alternatif_metin](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



Verilerde değişiklik yaptıktan sonra tıklayın.**Kayıt etmek** veya**Göndermek** değişikliklerinizi kaydetmek için

**Kaydet düğmesine tıklayarak değişiklikleri kaydetme** 

![yapılacaklar:resim_alternatif_metin](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Çözüm**
{{% alert color="primary" %}} 

Bu makale, bir çalışma sayfasının oluşturulan özel bir koleksiyona nasıl bağlanacağını gösterdi. Geliştiriciler, Aspose.Cells.GridWeb'i kullanarak çalışma sayfalarını bir GUI modunda veya kodlama yoluyla Çalışma Sayfaları Tasarımcısı aracılığıyla bir veritabanına veya özel koleksiyonlara bağlayabilir. Bu, geliştiricilere uygulama oluşturmak için çok çeşitli seçenekler sunar.

{{% /alert %}}
