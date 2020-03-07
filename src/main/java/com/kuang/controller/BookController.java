package com.kuang.controller;


import com.kuang.pojo.Books;
import com.kuang.service.BookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

@Controller
@RequestMapping("/book")
public class BookController {

    @Autowired
    @Qualifier("BookServiceImpl")
    private BookService bookService;
    @RequestMapping("/allbook")
    public String list(Model model){
         List<Books> list = bookService.queryAllBook();
         model.addAttribute("list",list);
        return "allBook";
    }

    @RequestMapping("toAddBook")
    public String toAdd(){
        return "addBook";
    }
    @RequestMapping("addBook")
    public String addPage(Books book){
        bookService.addBook(book);
        return "redirect:/book/allBook";
    }


    @RequestMapping("toUpdateBook")
    public String toUpdateBook(int id,Model model){
         Books books = bookService.queryBookById(id);
         model.addAttribute("books",books);
        return "updateBook";
    }
    @RequestMapping("/updateBook")
    public String updateBook(Model model,Books books){
        bookService.updateBook(books);
        Books book = bookService.queryBookById(books.getBookID());
        model.addAttribute("book",book);
        return "redirect:/book/allbook";
    }

    @RequestMapping("/del/{bookid}")
    public String del(@PathVariable("bookid") int id){
        bookService.deleteBookById(id);
        return "redirect:/book/allbook";
    }






}
