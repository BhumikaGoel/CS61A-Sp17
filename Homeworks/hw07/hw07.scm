(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond ((< x 0) -1)
        ((= x 0) 0)
        ((> x 0) 1)

  )
)

(define (square x) (* x x))

(define (pow b n)
    (cond ((equal? n 0) 1)
          ((equal? n 1) b)
          ((even? n) (square (pow b (/ n 2))))
          ((odd? n) (* b (pow b (- n 1)) ))))

    )
)

(define (ordered? s)
    (if (or (null? s) (null? (cdr s)))
        #t
        (and (<= (car s) (cadr s)) (ordered? (cdr s)))
    )

)

(define (nodots s)
    (define (containdots s)
        (and (pair? s) (not (or (pair? (cdr s)) (null? (cdr s)))))
    )

    (cond ((null? s) s)
        ((containdots s) (list (nodots (car s)) (cdr s)))
        ((pair? s) (cons (nodots (car s)) (nodots (cdr s))))
        (#t s)
    )
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ((> (car s) v) false)
          ((equal? (car s) v) true)
          (else (contains? (cdr s) v))
    )
)

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((< v (car s)) (cons v s))
          ((equal? v (car s)) s)
          ((> v (car s)) (cons (car s) (add (cdr s) v)))
    )
)

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          (else
              (define e1 (car s))
              (define e2 (car t))
              (cond ((equal? e1 e2) (cons e1 (intersect (cdr s) (cdr t))))
                    ((< e1 e2) (intersect (cdr s) t))
                    ((< e2 e1) (intersect s (cdr t)))

              )
          )
    )
)

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          (else
              (define e1 (car s))
              (define e2 (car t))
              (cond ((equal? e1 e2) (cons e1 (union (cdr s) (cdr t))))
                    ((< e1 e2) (cons e1 (union (cdr s) t)))
                    ((< e2 e1) (cons e2 (union s (cdr t))))

              )
          )
    )
)

; Q9 - Survey
(define (survey)
    ; Midsemester Survey: https://goo.gl/forms/DJozOAVLzfXARJGn2
    'parenthesis

)
