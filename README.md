# web-parsing-pdf-books-
ეს სკრიპტი წიგნის მონაცემების ამოღების საშუალებას გაძლევთ openlibrary.org ვებსაიტიდან, 
რითაც შეგიძლიათ მიიღოთ ინფორმაცია ტრენდული წიგნების შესახებ და შეინახოთ იგი 
csv ფაილის ფორმატში რაც ძალიან პრაქტიკული და მოსახერხებელია.განსაზღვრულია scrape_books ფუნქცია,
რომელიც იღებს ორ პარამეტრს: url ( ბიბლიოთეკის გვერდის URL,) და page_limit (გვერდების რაოდენობა, რომლებზეც უნდა ვიმუშაოთ).
ფუნქციის შიგნით, CSV ფაილი სახელად 'PDF_BOOKS.csv' იქმნება ჩაწერის რეჟიმში. სვეტის სათაურები (სათაური, ავტორი, გამოცემები) 
იწერება როგორც პირველი რიგი CSV ფაილში.
შემდეგ ფუნქცია ახორციელებს ციკლს 1-ლი გვერდიდან მითითებულ page_limit-მდე,რაც საშუალებას იძლევა ნავიგაცია მოახდინოს ვებსაიტის მრავალ გვერდზე მეტი მონაცემების მოსაპოვებლად.
თითოეული გვერდისთვის, HTTP GET მოთხოვნა კეთდება მოწოდებულ URL-ზე, პარამეტრად მიმდინარე გვერდის ნომრით,პასუხი მიიღება და ინახება.
BeautifulSoup-ის გამოყენებით შესაბამისი ინფორმაციის მოსაპოვებლად. სკრიპტი პოულობს HTML ელემენტებს, რომლებიც შეიცავს წიგნის ინფორმაციას, როგორიცაა სათაური, ავტორი და გამოცემები.
ამოღებული წიგნის ინფორმაცია შემდეგ იწერება CSV ფაილში.
