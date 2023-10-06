from . import feature_ext_upload
from . import views

class CompanyInfo():
    InfolistArray = []
    def Infolist(self, className):
            if('bmw' in className):
                company_Info1 = "The Company Details of bmw"
                self.InfolistArray.append(company_Info1)
                
            if('HP' in className):
                company_Info2 = "details of HP"
                self.InfolistArray.append(company_Info2)
                
            if('adidas' in className):
                company_Info3 = "details of addidas"
                self.InfolistArray.append(company_Info3)
                
            if( 'aldi' in className):
                company_Info4 = "details of aldi"
                self.InfolistArray.append(company_Info4)
                
            return self.InfolistArray   
        
        
    def brand_Info(self, queried_class_name):
        
        if(queried_class_name[0] == 'HP'):
            brand_info = "HP Info"
            brand_link = "https://www.hp.com/us-en/home.html"
        elif(queried_class_name[0] == 'adidas'):
            brand_info = "The company was started by Adolf Dassler in his mother's house. He was joined by his elder brother Rudolf in 1924 under the name Gebrüder Dassler Schuhfabrik ("'Dassler Brothers Shoe Factory'").Dassler assisted in the development of spiked running shoes (spikes) for multiple athletic events. To enhance the quality of spiked athletic footwear, he transitioned from a previous model of heavy metal spikes to utilising canvas and rubber. Dassler persuaded U.S. sprinter Jesse Owens to use his handmade spikes at the 1936 Summer Olympics. In 1949, following a breakdown in the relationship between the brothers, Adolf created Adidas and Rudolf established Puma, which became Adidas's business rival.[1]"
            brand_link = "https://www.adidas.com/us"   
        elif(queried_class_name[0] == 'aldi'):
            brand_info = "Aldi's German operations consist of Aldi Nord's 35 individual regional companies with about 2,200 stores in western, northern, and eastern Germany, and Aldi Süd's 32 regional companies with 2,000 stores in western and southern Germany.[10] Internationally, Aldi Nord operates in Belgium, Denmark, France, Luxembourg, Poland, Portugal and Spain, while Aldi Süd operates in Australia, Austria, China, Hungary, Ireland, Italy, Slovenia, Switzerland, United Kingdom and United States. Only in Austria and Slovenia Aldi operates the stores under the Hofer brand. Aldi Nord also owns the Trader Joe's grocery chain in the United States which operates separately from the group.[11][12] Aldi announced in August 2023 that it will buy 400 Winn-Dixie and Harveys supermarkets in the southern United States."
            brand_link = "https://www.aldi.co.uk/"
        elif(queried_class_name[0] == 'apple'):
            brand_info = "Apple was founded as Apple Computer Company on April 1, 1976, by Steve Wozniak, Steve Jobs (1955–2011) and Ronald Wayne to develop and sell Wozniak's Apple I personal computer. It was incorporated by Jobs and Wozniak as Apple Computer, Inc. in 1977. The company's second computer, the Apple II, became a best seller and one of the first mass-produced microcomputers. Apple went public in 1980 to instant financial success. The company developed computers featuring innovative graphical user interfaces, including the 1984 original Macintosh, announced that year in a critically acclaimed advertisement called "'1984'". By 1985, the high cost of its products, and power struggles between executives, caused problems. Wozniak stepped back from Apple and pursued other ventures, while Jobs resigned and founded NeXT, taking some Apple employees with him."
            brand_link = "https://www.apple.com/"
        elif(queried_class_name[0] == 'becks'):
            brand_info = "Beck's Brewery, also known as Brauerei Beck & Co., is a brewery in the northern German city of Bremen. In 2001, Interbrew bought Brauerei Beck for 1.8 billion euros; at that time it was the fourth-largest brewer in Germany.[2] US manufacture of Beck's has been based in St. Louis, Missouri, since early 2012.[3].The Beck's brewery in Bremen. The Beck's Brewery beer Haake-Beck sponsors Bundesliga club Werder Bremen.Since 2008, it has been owned by Anheuser-Busch InBev SA/NV subsidiary Interbrew.[4][5].Beck's key logo is based upon the city of Bremen's coat of arms, which contains a key attributed to the patron saint of the city, Saint Peter.The brewery sponsored Jaguar in Formula 1 until 2004."
            brand_link = "https://www.beck.com/"
        elif(queried_class_name[0] == 'bmw'):
            brand_info = "BMW is headquartered in Munich and produces motor vehicles in Germany, Brazil, China, India, Mexico, the Netherlands, South Africa, the United Kingdom, and the United States. The Quandt family is a long-term shareholder of the company, following investments by the brothers Herbert and Harald Quandt in 1959 that saved BMW from bankruptcy, with the remaining shares owned by the public."
            brand_link = "https://www.bmw.com/en/index.html"
        elif(queried_class_name[0] == 'carlsberg'):
            brand_info = "Carlsberg A/S (/ˈkɑːrlzbɜːrɡ/; Danish: [ˈkʰɑˀlsˌpɛɐ̯ˀ]) is a Danish multinational brewer. Founded in 1847 by J. C. Jacobsen, the company's headquarters is in Copenhagen, Denmark. Since Jacobsen's death in 1887, the majority owner of the company has been the Carlsberg Foundation. The company's flagship brand is Carlsberg (named after Jacobsen's son Carl). Other brands include Tuborg, Kronenbourg, Somersby cider, Holsten, Neptun, Belgian Grimbergen, Fix, one of Greece's oldest brands and more than 500 local beers.[5][failed verification] The company employs around 41,000 people, primarily in Europe and Asia. Carlsberg is currently the 6th largest brewery in the world based on revenue."
            brand_link = "https://www.carlsberggroup.com/"
        elif(queried_class_name[0] == 'chimay'):
            brand_info = "The brewery was founded inside Scourmont Abbey, in the Belgian municipality of Chimay in 1862.[1] The brewery produces four ales as well as a patersbier for the monks themselves which is occasionally sold as Chimay Gold; they are known as Trappist beers because they are made in a Trappist monastery. It was the first brewery to use the Trappist Ale designation on its labels."
            brand_link = "https://chimay.com/en/"
        elif(queried_class_name[0] == 'cocacola'):
            brand_info = "Coca-Cola, or Coke, is a carbonated soft drink manufactured by the Coca-Cola Company. In 2013, Coke products were sold in over 200 countries worldwide, with consumers drinking more than 1.8 billion company beverage servings each day.[1] Coca-Cola ranked No. 87 in the 2018 Fortune 500 list of the largest United States corporations by total revenue.[2] Based on Interbrand's "'best global brand'" study of 2020, Coca-Cola was the world's sixth most valuable brand."
            brand_link = "https://www.coca-colacompany.com/"
        elif(queried_class_name[0] == 'corona'):
            brand_info = "Corona beer, a Mexican-born brew with a distinct flavor and iconic branding, has left an indelible mark on the beer industry."
            brand_link = "https://www.corona.com/en"
        elif(queried_class_name[0] == 'dhl'):
            brand_info = "DHL[4] is an American-founded German logistics company[5] providing courier, package delivery and express mail service, delivering over 1.8 billion parcels per year.[6] A subsidiary of the German logistics firm DHL Group, its express mail service DHL Express is one of the market leaders for parcel services in Europe and Germany's main courier and parcel service."
            brand_link = "https://www.dhl.com/"
        elif(queried_class_name[0] == 'erdinger'):
            brand_info = "Erdinger is the world's largest wheat beer brewery. It is widely available and popular across Germany and the European Union. Erdinger was founded in 1886 by Johann Kienle. Erdinger beer is the best-known culinary product of the town; however, the brewery did not receive its current name until 1949 from its owner Franz Brombach, who had acquired the brewery 14 years earlier. The current owner is Franz Brombach's son, Werner Brombach (since 1975)."
            brand_link = "https://int.erdinger.de/"
        elif(queried_class_name[0] == 'esso'):
            brand_info = "Standard Oil of New Jersey started marketing its products under the Esso brand[3] in 1926.[4] In 1972, the name Esso was largely replaced in the U.S. by the Exxon brand after the Standard Oil of New Jersey bought Humble Oil, while the Esso name remained widely used elsewhere. In most of the world, the Esso brand and the Mobil brand are the primary brand names of ExxonMobil, while the Exxon brand is used only in the United States alongside Mobil."
            brand_link = "https://www.esso.com/en"
        elif(queried_class_name[0] == 'fedex'):
            brand_info = "FedEx Corporation, formerly Federal Express Corporation and later FDX Corporation, is an American multinational conglomerate holding company focused on transportation, e-commerce and business services based in Memphis, Tennessee.[3][4] The name "'FedEx'" is a syllabic abbreviation of the name of the company's original air division, Federal Express, which was used from 1973 until 2000. FedEx today is best known for its air delivery service, FedEx Express, which was one of the first major shipping companies to offer overnight delivery as a flagship service. Since then, FedEx also started FedEx Ground, FedEx Office (originally known as Kinko's), FedEx Supply Chain, FedEx Freight, and various other services across multiple subsidiaries, often meant to respond to its main competitor, UPS. The company is the fifth largest American-headquartered employer globally with 547,000 employees, and FedEx is also one of the top contractors of the US government and assists in the transport of some United States Postal Service packages through their Air Cargo Network contract."
            brand_link = "https://www.fedex.com/"
        elif(queried_class_name[0] == 'ferrari'):
            brand_info = "Ferrari S.p.A. (/fəˈrɑːri/; Italian: [ferˈraːri]) is an Italian luxury sports car manufacturer based in Maranello, Italy. Founded in 1939 by Enzo Ferrari (1898–1988), the company built its first car, a sports racing car, in 1940. It adopted its current name in 1945, and began to produce its current line of road cars in 1947. Ferrari became a public company in 1960, and from 1963 to 2014 it was a subsidiary of Fiat S.p.A. It was spun off from Fiat's successor entity, Fiat Chrysler Automobiles, in 2016."
            brand_link = "https://www.ferrari.com/"
        elif(queried_class_name[0] == 'ford'):
            brand_info = "Ford Motor Company (commonly known as Ford) is an American multinational automobile manufacturer headquartered in Dearborn, Michigan, United States. It was founded by Henry Ford and incorporated on June 16, 1903. The company sells automobiles and commercial vehicles under the Ford brand, and luxury cars under its Lincoln brand. Ford also owns a 32% stake in China's Jiangling Motors.[8] It also has joint ventures in China (Changan Ford), Taiwan (Ford Lio Ho), Thailand (AutoAlliance Thailand), and Turkey (Ford Otosan). The company is listed on the New York Stock Exchange and is controlled by the Ford family; they have minority ownership but the majority of the voting power."
            brand_link = "https://www.ford.com/"
        elif(queried_class_name[0] == 'fosters'):
            brand_info = "Foster's Lager is an Australian internationally distributed brand of Australian lager. It is owned by the international brewing group Asahi Group Holdings, and is brewed under licence in a number of countries, including its biggest market, the UK, where the European rights to the brand are owned by Heineken International."
            brand_link = "https://www.fostersbeer.com/"
        elif(queried_class_name[0] == 'google'):
            brand_info = "Google was founded on September 4, 1998, by American computer scientists Larry Page and Sergey Brin while they were PhD students at Stanford University in California. Together they own about 14% of its publicly listed shares and control 56% of its stockholder voting power through super-voting stock. The company went public via an initial public offering (IPO) in 2004. In 2015, Google was reorganized as a wholly owned subsidiary of Alphabet Inc. Google is Alphabet's largest subsidiary and is a holding company for Alphabet's internet properties and interests. Sundar Pichai was appointed CEO of Google on October 24, 2015, replacing Larry Page, who became the CEO of Alphabet. On December 3, 2019, Pichai also became the CEO of Alphabet."
            brand_link = "https://about.google/"
        elif(queried_class_name[0] == 'guiness'):
            brand_info = "Guinness (/ˈɡɪnəs/) is an Irish dry stout that originated in the brewery of Arthur Guinness at St. James's Gate, Dublin, Ireland, in 1759. It is one of the most successful alcohol brands worldwide, brewed in almost 50 countries, and available in over 120.[2][3] Sales in 2011 amounted to 850,000,000 liters (190,000,000 imp gal; 220,000,000 U.S. gal).[2] In spite of declining consumption since 2001,[4] it is the best-selling alcoholic drink in Ireland[5] where Guinness & Co. Brewery makes almost €2 billion worth of beer annually."
            brand_link = "https://www.guinness.com/"
        elif(queried_class_name[0] == 'heineken'):
            brand_info = "heineken Info"
            brand_link = ""
        elif(queried_class_name[0] == 'milka'):
            brand_info = "milka Info"
            brand_link = ""
        elif(queried_class_name[0] == 'nvidia'):
            brand_info = "nvidia Info"
            brand_link = ""
        elif(queried_class_name[0] == 'paulaner'):
            brand_info = "paulaner Info"
            brand_link = ""
        elif(queried_class_name[0] == 'pepsi'):
            brand_info = "pepsi Info"
            brand_link = ""
        elif(queried_class_name[0] == 'rittersport'):
            brand_info = "rittersport Info"
            brand_link = ""
        elif(queried_class_name[0] == 'shell'):
            brand_info = "shell Info"
            brand_link = ""
        elif(queried_class_name[0] == 'singha'):
            brand_info = "singha Info"
            brand_link = ""
        elif(queried_class_name[0] == 'starbucks'):
            brand_info = "starbucks Info"
            brand_link = "Foster's Lager is an Australian internationally distributed brand of Australian lager. It is owned by the international brewing group Asahi Group Holdings, and is brewed under licence in a number of countries, including its biggest market, the UK, where the European rights to the brand are owned by Heineken International."
        elif(queried_class_name[0] == 'stellaartois'):
            brand_info = "Stella Artois (/ɑːrˈtwɑː/ ar-TWAH, French: [aʁtwɑ]) is a pilsner beer,[1] first brewed in 1926 by Brouwerij Artois in Leuven, Belgium. In its original form, the beer is 5.2 per cent ABV, the country's standard for pilsners. The beer is also sold in other countries including the UK, Ireland, Canada and Australia, where it has a reduced ABV.[4][5] Stella Artois is owned by Interbrew International B.V. which is a subsidiary of the world's largest brewer, Anheuser-Busch InBev SA/NV."
            brand_link = "https://www.stellaartois.com/"
        elif(queried_class_name[0] == 'texaco'):
            brand_info = "Texaco gasoline comes with Techron, an additive developed by Chevron, as of 2005, replacing the previous CleanSystem3. The Texaco brand is strong in the U.S., Latin America, and West Africa. It has a presence in Europe as well; for example, it is a well-known retail brand in the UK, with around 980 Texaco-branded service stations."
            brand_link = "https://www.texaco.com/"
        elif(queried_class_name[0] == 'tsingtao'):
            brand_info = "Tsingtao Brewery Co. Ltd. (simplified Chinese: 青岛啤酒厂; traditional Chinese: 青島啤酒廠; pinyin: Qīngdǎo Píjiǔchǎng) is China's second largest brewery, with about 15% of domestic market share and also accounts for half of China's national beer exports.[2][3][4] It was founded in 1903 by German settlers in Tsingtau (Qingdao), Kiautschou Bay Leased Territory. In 2016, Tsingtao was the second most consumed beer globally and had reached 2.8% share of the global beer market, after its share of the world's beer market had been steadily growing by at least 0.1 percentage points every year since 2009.[5] Tsingtao is currently the sixth largest brewery in the world. Its logo displays an image of Huilan Pavilion that stands on the end of Zhanqiao Pier, located on Qingdao's southern shore."
            brand_link = "https://www.tsingtao.com/"
        elif(queried_class_name[0] == 'ups'):
            brand_info = "Discover fast, reliable global shipping and logistics solutions with UPS. Explore our services and streamline your supply chain today. Need to ship packages across the world? Let UPS be your logistics partner. Explore our services and simplify your shipping process."
            brand_link = "https://www.ups.com/us/en/Home.page"
        elif(queried_class_name[0] == 'no-logo'):
            brand_info = "no logo category."
            brand_link = ""
        else:
            brand_info = "NOt related to the Logo or Brands."
            
        return brand_info, brand_link
    
    
    def queriedAccuracy(self, insertknnclasses):
        length_total = len(insertknnclasses)
        mysetlist = list(set(insertknnclasses))
        length_mysetlist = len(mysetlist)
        similar_class = length_total - length_mysetlist
        similarity_ratio = ((similar_class) *100) / length_total
        
        return int(similarity_ratio)
        