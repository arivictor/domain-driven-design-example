import application.book.event


def notify_customers_new_book_added(event: application.book.event.BookAdded):
    print(f"[domain-event] A new book has been added: {event.title} by {event.author}")
