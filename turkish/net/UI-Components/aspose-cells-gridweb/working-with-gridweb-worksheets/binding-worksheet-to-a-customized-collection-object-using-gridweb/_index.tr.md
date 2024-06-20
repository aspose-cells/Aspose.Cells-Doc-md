---
title: GridWeb Kullanarak Özelleştirilmiş Bir Koleksiyon Nesnesine Çalışma Sayfası Bağlama
type: docs
weight: 130
url: /tr/net/aspose-cells-gridweb/bind-worksheet-to-a-customized-collection-object-using-gridweb/
keywords: GridWeb,bind
description: Bu makale, GridWeb de bir koleksiyona çalışma sayfası bağlamanın nasıl yapılacağını tanıtmaktadır. 
---

{{% alert color="primary" %}} 

.NET Framework, birçok koleksiyon sınıfı sunar, ancak bazen geliştirme gereksinimlerini karşılamazlar, bu nedenle geliştiriciler **özel koleksiyonlar** oluştururlar ve GridWeb'de bir çalışma sayfasını böylesi özel koleksiyonlarla bağlayabilirsiniz.

{{% /alert %}} 
## **Özel Bir Koleksiyonla Çalışma Sayfası Bağlama**
Bu özelliği göstermek için bu makale, adım adım bir örnek uygulama nasıl oluşturulacağı üzerinden ilerlemektedir. İlk olarak, özel bir koleksiyon oluşturun ve ardından bu koleksiyonu bir çalışma sayfası ile bağlantılı olarak kullanın.
### **Adım 1: Özel Bir Kayıt Oluşturma**
Özel bir koleksiyon oluşturmadan önce, koleksiyonda depolanacak özel kayıtları tutan bir sınıf oluşturun. Bu makalenin amacı, kendi özel koleksiyonlarınızı nasıl oluşturacağınıza dair bir fikir vermek olduğundan özel kaydı nasıl oluşturacağınız size kalmıştır.

Aşağıdaki örnek, beş özel alan içeren ve bu özel alanlara erişimi kontrol eden beş genel özelliği olan MyCustomRecord sınıfını kullanır. İşte özelliklerin yapısı: 

- **StringField1** (dize) okumak ve yazmak için StringField1 özelliği.
- **StringField2** (dize) sadece okumak için ReadonlyField2 özelliği.
- **datefield1** (TarihZaman) okumak ve yazmak için DateField1 özelliği.
- **intfield1** (tamsayı) okumak ve yazmak için IntField1 özelliği.
- **doublefield1** (kesirli sayı) okumak ve yazmak için DoubleField1 özelliği.

**C#**

{{< highlight csharp >}}

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
### **Adım 2: Özel Bir Koleksiyon Oluşturma**
Şimdi, müşteri kayıtlarını eklemek ve erişmek için özel bir koleksiyon oluşturun. Basit tutmak için, bu örnek MyCollection sınıfını kullanır, içinde salt okunur bir indeksleyici içerir. Bu indeksleyiciyi kullanarak, koleksiyonda depolanan herhangi bir özel kayda erişebiliriz.

**C#**

{{< highlight csharp >}}

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
### **Adım 3: Bir Çalışsayıyı Özel Bir Koleksiyon ile Bağlama**
Özel bir koleksiyon oluşturma süreci tamamlandı. Şimdi, özel koleksiyonu Aspose.Cells.GridWeb ile bir çalış sayıya bağlamak için kullanın. İlk önce bir web form oluşturun, üzerine GridWeb kontrolünü ekleyin ve biraz kod ekleyin.

Bağlamak için özel koleksiyonu kullanmak için önce MyCollection sınıfından bir nesne oluşturun (yukarıdaki adımda oluşturulmuştur).
Ardından MyCollection nesneleri oluşturun ve MyCollection nesnesine ekleyin.

{{% alert color="primary" %}} 

MyCollection sınıfında bir MyCustomRecord nesnesini koleksiyona eklemek için bir yöntem olmadığını düşünüyor musunuz? Yukarıdaki kodlara tekrar bakın ve MyCollection sınıfının (nesne topluluğuna bir nesne eklemek için Add yöntemini sağlayan IList arabirimini uygulamış olan) CollectionBase sınıfından miras alındığını fark edeceksiniz. MyCollection nesnesini IList'e yükseltme yaparak IList sınıfının Add yöntemini kullanın.

{{% /alert %}} 

Son olarak, MyCollection nesnesini çalış sayısının veri kaynağı olarak ayarlayın ve çalış sayısını koleksiyonla bağlayın. Bu noktada, çalış sayısının bağlı sütunları için doğrulama kuralları da oluşturabilirsiniz.

**C#**

{{< highlight csharp >}}

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
### **Adım 4: Çalış Sayısının InitializeNewBindRow Olayını İşleme**
Yukarıdaki kodlarda, çalış sayısının InitializeNewBindRow olayına GridWeb1_InitializeNewBindRow olay işleyicisini atamak için kullanılan ek bir kod satırı fark etmiş olabilirsiniz. Bu olay, çalış sayısına yeni bağlı bir satır eklendiğinde tetiklenir. Bu olay için bir olay işleyici oluşturduk çünkü MyCustomRecord nesnesinin DateField1 özelliğinden dolayı.

Aspose.Cells.GridWeb, yeni bağlı bir satır çalış sayısına eklendiğinde **sıfır (0)** değeri ile **int** ve **double** değerlerini otomatik olarak başlatır. Tarihler için, GridWeb kontrolünün sistemin güncel tarihini otomatik olarak eklemesini istiyoruz. Bunu yapmak için GridWeb1_InitializeNewBindRow olay işleyicisini InitializeNewBindRow olayı için oluşturduk.

GridWeb'den MyCustomRecord sınıfının belirli bir örneğine bağlanılmış nesnesi kullanarak ve ardından mevcut sistem tarihini TarihZaman1 özelliğine atayın.

**C#**

{{< highlight csharp >}}

 //Creating GridWeb1_InitializeNewBindRow event handler

private void GridWeb1_InitializeNewBindRow(GridWorksheet sender, object bindObject)

{

    //Accessing that custom record object that is newly bound

    MyCustomRecord rec = (MyCustomRecord)bindObject;

    //Initializing the DateTime of a property when a new row gets bound to the database

    rec.DateField1 = DateTime.Now;

}

{{< /highlight >}}
### **Adım 5: Uygulamanın Çalıştırılması**
Uygulamayı ya **Ctrl+F5** tuşlarına basarak ya da VS.NET'te **Başlat** düğmesine tıklayarak çalıştırın. Web formu yeni bir tarayıcı penceresinde açılır. 

**Özel koleksiyonla bağlı çalış sayısı** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_1.png)



GridWeb kontrolüne sağ tıklayarak bir kayıt ekleyin veya silin. Örneğin, **Satır Ekle** seçeneğini seçerek çalış sayısına yeni bir kayıt ekleyin. 

**Menüden Satır Ekle seçeneğini seçme** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_2.png)



Çalış sayısına yeni bir satır eklendiğinde, hücreler, güncel sistem tarihi de dahil olmak üzere varsayılan verileri içerir. 

**Varsayılan verilerle çalış sayısına yeni satır eklendi** 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_3.png)



Verilere değişiklik yapmak için **Kaydet** veya **Gönder** düğmesine tıklayın. 

**Kaydet** düğmesine tıklayarak değişiklikleri kaydetme 

![todo:image_alt_text](binding-worksheet-to-a-customized-collection-object-using-gridweb_4.png)
## **Sonuç**
{{% alert color="primary" %}} 

Bu makale, oluşturulan bir özel koleksiyona bir çalış sayısını nasıl bağlayacağını gösterdi. Aspose.Cells.GridWeb kullanarak geliştiriciler, çalış sayılarını ya veritabanına ya da çalış tasarımcısı aracılığıyla veya kodlama yoluyla özel koleksiyonlara bağlayabilir. Bu, geliştiricilere uygulamalar oluşturmak için geniş bir seçenek yelpazesi sunar.

{{% /alert %}}
